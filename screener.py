"""
EOD trading-value screener for HK equities.

Identifies stocks whose latest session turnover (Close × Volume) moved by at
least ±20% versus the prior trading session, using only in-memory historical data.
"""

from __future__ import annotations

import logging

import numpy as np
import pandas as pd

logger = logging.getLogger(__name__)

# Minimum turnover on the latest session to filter illiquid names (HKD).
_MIN_TURNOVER_TODAY_HKD = 15_000_000

# Turnover ratio thresholds: >= 1.20 (20%+ increase) or <= 0.80 (20%+ decrease).
_RATIO_INCREASE_THRESHOLD = 1.20
_RATIO_DECREASE_THRESHOLD = 0.80


def _resolve_latest_trading_dates(df: pd.DataFrame) -> tuple[pd.Timestamp, pd.Timestamp]:
    """
    Determine the two most recent valid trading dates present in the dataset.

    Uses the union of all dates with non-zero, non-NaN volume across tickers
    rather than calendar offsets, so weekends and HKEX holidays are handled
    implicitly from the market data itself.
    """
    if df.empty:
        raise ValueError("Cannot resolve trading dates from an empty DataFrame")

    working = df.reset_index() if isinstance(df.index, pd.MultiIndex) else df.copy()
    if "Date" not in working.columns:
        raise ValueError("DataFrame must contain a Date column or MultiIndex level")

    valid = working.dropna(subset=["Volume"])
    valid = valid[valid["Volume"] > 0]

    if valid.empty:
        raise ValueError("No rows with positive volume found in dataset")

    unique_dates = sorted(valid["Date"].unique())
    if len(unique_dates) < 2:
        raise ValueError(
            f"Need at least 2 trading dates in data; found {len(unique_dates)}"
        )

    date_today = pd.Timestamp(unique_dates[-1])
    date_yesterday = pd.Timestamp(unique_dates[-2])
    return date_today, date_yesterday


def screen_value_changes(df: pd.DataFrame) -> pd.DataFrame:
    """
    Screen for significant day-over-day trading value (turnover) changes.

    Parameters
    ----------
    df:
        Master market DataFrame (MultiIndex [Ticker, Date] or long format) with
        at least Volume and Close columns.

    Returns
    -------
    pd.DataFrame
        Sorted results with columns:
        Ticker, Date_Today, Date_Prev, Volume_Today, Volume_Prev,
        Close_Today, Price_Pct_Change, Value_Pct_Change
    """
    empty_result = pd.DataFrame(
        columns=[
            "Ticker",
            "Date_Today",
            "Date_Prev",
            "Volume_Today",
            "Volume_Prev",
            "Close_Today",
            "Price_Pct_Change",
            "Value_Pct_Change",
        ]
    )

    if df is None or df.empty:
        logger.warning("Screener received empty input; returning no alerts")
        return empty_result

    working = df.reset_index() if isinstance(df.index, pd.MultiIndex) else df.copy()

    required = {"Ticker", "Date", "Volume", "Close"}
    missing = required - set(working.columns)
    if missing:
        raise ValueError(f"Input DataFrame missing required columns: {sorted(missing)}")

    # Drop sessions with no trading activity (halts, missing data).
    working = working.dropna(subset=["Volume", "Close"])
    working = working[(working["Volume"] > 0) & (working["Close"] > 0)]

    if working.empty:
        logger.warning("No positive-volume rows remain after filtering")
        return empty_result

    try:
        date_today, date_prev = _resolve_latest_trading_dates(working)
    except ValueError as exc:
        logger.warning("Could not resolve trading dates: %s", exc)
        return empty_result

    logger.info(
        "Comparing turnover: latest session=%s, prior session=%s",
        date_today.date(),
        date_prev.date(),
    )

    today_rows = working[working["Date"] == date_today][
        ["Ticker", "Volume", "Close"]
    ].rename(columns={"Volume": "Volume_Today", "Close": "Close_Today"})
    prev_rows = working[working["Date"] == date_prev][
        ["Ticker", "Volume", "Close"]
    ].rename(columns={"Volume": "Volume_Prev", "Close": "Close_Prev"})

    merged = today_rows.merge(prev_rows, on="Ticker", how="inner")

    merged["Turnover_Today"] = merged["Volume_Today"] * merged["Close_Today"]
    merged["Turnover_Prev"] = merged["Volume_Prev"] * merged["Close_Prev"]

    # Baseline liquidity filter on today's turnover (HKD).
    merged = merged[merged["Turnover_Today"] > _MIN_TURNOVER_TODAY_HKD]

    if merged.empty:
        logger.info(
            "No tickers passed the HKD %d turnover floor",
            _MIN_TURNOVER_TODAY_HKD,
        )
        return empty_result

    # Guard against zero/NaN prior turnover (division-by-zero and halt artifacts).
    merged = merged.dropna(subset=["Turnover_Prev", "Close_Prev"])
    merged = merged[merged["Turnover_Prev"] > 0]
    merged = merged[merged["Close_Prev"] > 0]

    if merged.empty:
        logger.info("No tickers with valid prior-session turnover")
        return empty_result

    merged["Value_Ratio"] = merged["Turnover_Today"] / merged["Turnover_Prev"]
    merged["Value_Pct_Change"] = (merged["Value_Ratio"] - 1.0) * 100.0
    merged["Price_Pct_Change"] = (
        (merged["Close_Today"] / merged["Close_Prev"]) - 1.0
    ) * 100.0

    alerts = merged[
        (merged["Value_Ratio"] >= _RATIO_INCREASE_THRESHOLD)
        | (merged["Value_Ratio"] <= _RATIO_DECREASE_THRESHOLD)
    ].copy()

    alerts["Date_Today"] = date_today
    alerts["Date_Prev"] = date_prev
    alerts["Volume_Today"] = alerts["Volume_Today"].astype(np.int64)
    alerts["Volume_Prev"] = alerts["Volume_Prev"].astype(np.int64)
    alerts["Value_Pct_Change"] = alerts["Value_Pct_Change"].round(2)
    alerts["Price_Pct_Change"] = alerts["Price_Pct_Change"].round(2)

    result = alerts[
        [
            "Ticker",
            "Date_Today",
            "Date_Prev",
            "Volume_Today",
            "Volume_Prev",
            "Close_Today",
            "Price_Pct_Change",
            "Value_Pct_Change",
        ]
    ].sort_values("Value_Pct_Change", ascending=False, key=abs)

    logger.info("Screener found %d value alerts", len(result))
    return result.reset_index(drop=True)
