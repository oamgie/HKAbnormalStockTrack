"""
EOD volume-change screener for HK equities.

Identifies stocks whose latest trading volume moved by at least ±20% versus
the prior trading session, using only in-memory historical data.
"""

from __future__ import annotations

import logging

import numpy as np
import pandas as pd

logger = logging.getLogger(__name__)

# Minimum shares traded on the latest session to filter illiquid names.
_MIN_VOLUME_TODAY = 100_000

# Volume ratio thresholds: >= 1.20 (20%+ increase) or <= 0.80 (20%+ decrease).
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


def screen_volume_changes(df: pd.DataFrame) -> pd.DataFrame:
    """
    Screen for significant day-over-day volume changes.

    Parameters
    ----------
    df:
        Master market DataFrame (MultiIndex [Ticker, Date] or long format) with
        at least a Volume column.

    Returns
    -------
    pd.DataFrame
        Sorted results with columns:
        Ticker, Date_Today, Date_Prev, Volume_Today, Volume_Prev, Pct_Change
    """
    empty_result = pd.DataFrame(
        columns=[
            "Ticker",
            "Date_Today",
            "Date_Prev",
            "Volume_Today",
            "Volume_Prev",
            "Pct_Change",
        ]
    )

    if df is None or df.empty:
        logger.warning("Screener received empty input; returning no alerts")
        return empty_result

    working = df.reset_index() if isinstance(df.index, pd.MultiIndex) else df.copy()

    required = {"Ticker", "Date", "Volume"}
    missing = required - set(working.columns)
    if missing:
        raise ValueError(f"Input DataFrame missing required columns: {sorted(missing)}")

    # Drop sessions with no trading activity (halts, missing data).
    working = working.dropna(subset=["Volume"])
    working = working[working["Volume"] > 0]

    if working.empty:
        logger.warning("No positive-volume rows remain after filtering")
        return empty_result

    try:
        date_today, date_prev = _resolve_latest_trading_dates(working)
    except ValueError as exc:
        logger.warning("Could not resolve trading dates: %s", exc)
        return empty_result

    logger.info(
        "Comparing volumes: latest session=%s, prior session=%s",
        date_today.date(),
        date_prev.date(),
    )

    today_rows = working[working["Date"] == date_today][["Ticker", "Volume"]].rename(
        columns={"Volume": "Volume_Today"}
    )
    prev_rows = working[working["Date"] == date_prev][["Ticker", "Volume"]].rename(
        columns={"Volume": "Volume_Prev"}
    )

    merged = today_rows.merge(prev_rows, on="Ticker", how="inner")

    # Baseline liquidity filter on today's volume.
    merged = merged[merged["Volume_Today"] > _MIN_VOLUME_TODAY]

    if merged.empty:
        logger.info("No tickers passed the %d-share liquidity floor", _MIN_VOLUME_TODAY)
        return empty_result

    # Guard against zero/NaN prior volume (division-by-zero and halt artifacts).
    merged = merged.dropna(subset=["Volume_Prev"])
    merged = merged[merged["Volume_Prev"] > 0]

    if merged.empty:
        logger.info("No tickers with valid prior-session volume")
        return empty_result

    merged["Ratio"] = merged["Volume_Today"] / merged["Volume_Prev"]
    merged["Pct_Change"] = (merged["Ratio"] - 1.0) * 100.0

    alerts = merged[
        (merged["Ratio"] >= _RATIO_INCREASE_THRESHOLD)
        | (merged["Ratio"] <= _RATIO_DECREASE_THRESHOLD)
    ].copy()

    alerts["Date_Today"] = date_today
    alerts["Date_Prev"] = date_prev
    alerts["Volume_Today"] = alerts["Volume_Today"].astype(np.int64)
    alerts["Volume_Prev"] = alerts["Volume_Prev"].astype(np.int64)
    alerts["Pct_Change"] = alerts["Pct_Change"].round(2)

    result = alerts[
        [
            "Ticker",
            "Date_Today",
            "Date_Prev",
            "Volume_Today",
            "Volume_Prev",
            "Pct_Change",
        ]
    ].sort_values("Pct_Change", ascending=False, key=abs)

    logger.info("Screener found %d volume alerts", len(result))
    return result.reset_index(drop=True)
