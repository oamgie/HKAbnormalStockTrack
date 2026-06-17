"""
Concurrent yfinance data fetcher for HK equities.

Uses batched ``yf.download`` calls (far fewer HTTP requests than per-ticker
``Ticker.history``) and suppresses noisy yfinance delisting logs for symbols
that simply return no rows.
"""

from __future__ import annotations

import logging
from typing import Iterable

import pandas as pd
import yfinance as yf

logger = logging.getLogger(__name__)

# Number of calendar days to request; covers long weekends and HK/public holidays.
_LOOKBACK_PERIOD = "5d"

# Symbols per yf.download call — balances payload size vs. request count.
_DEFAULT_BATCH_SIZE = 100


def _chunked(items: list[str], size: int) -> Iterable[list[str]]:
    """Yield successive fixed-size chunks from a list."""
    for start in range(0, len(items), size):
        yield items[start : start + size]


def _parse_download_batch(raw: pd.DataFrame, tickers: list[str]) -> list[pd.DataFrame]:
    """
    Convert a yf.download result into per-ticker long-format frames.

    Skips symbols with no rows or zero volume across the lookback window.
    """
    if raw is None or raw.empty:
        return []

    frames: list[pd.DataFrame] = []

    # Single-ticker downloads use flat columns; multi-ticker uses a MultiIndex.
    if not isinstance(raw.columns, pd.MultiIndex):
        ticker = tickers[0]
        frame = _normalize_history_frame(raw, ticker)
        if frame is not None:
            frames.append(frame)
        return frames

    available = set(raw.columns.get_level_values(0))
    for ticker in tickers:
        if ticker not in available:
            continue
        frame = _normalize_history_frame(raw[ticker], ticker)
        if frame is not None:
            frames.append(frame)

    return frames


def _impute_missing_close(frame: pd.DataFrame) -> pd.DataFrame:
    """
    Fill missing Close prices when Yahoo returns volume but omits the EOD close.

    Uses the High/Low midpoint first, then Open as a last resort.
    """
    if "Close" not in frame.columns or not frame["Close"].isna().any():
        return frame

    missing = frame["Close"].isna()
    hl_ok = missing & frame["High"].notna() & frame["Low"].notna()
    frame.loc[hl_ok, "Close"] = (frame.loc[hl_ok, "High"] + frame.loc[hl_ok, "Low"]) / 2

    missing = frame["Close"].isna()
    open_ok = missing & frame["Open"].notna()
    frame.loc[open_ok, "Close"] = frame.loc[open_ok, "Open"]

    return frame


def _normalize_history_frame(history: pd.DataFrame, ticker: str) -> pd.DataFrame | None:
    """Validate and standardize one ticker's OHLCV history."""
    if history is None or history.empty:
        return None

    working = history.dropna(how="all")
    if working.empty or "Volume" not in working.columns:
        return None

    # Drop symbols with no actual trading activity in the window.
    if working["Volume"].fillna(0).sum() <= 0:
        return None

    frame = working.reset_index()
    date_col = "Date" if "Date" in frame.columns else frame.columns[0]
    frame = frame.rename(columns={date_col: "Date"})

    frame["Date"] = pd.to_datetime(frame["Date"], utc=True).dt.tz_convert(None).dt.normalize()
    frame["Ticker"] = ticker
    frame = _impute_missing_close(frame)

    # Drop rows that still lack a usable close after imputation.
    frame = frame.dropna(subset=["Close"])
    frame = frame[frame["Close"] > 0]
    if frame.empty:
        return None

    return frame[["Ticker", "Date", "Open", "High", "Low", "Close", "Volume"]]


def _download_batch(tickers: list[str]) -> list[pd.DataFrame]:
    """Download one batch of tickers via yfinance."""
    if not tickers:
        return []

    try:
        raw = yf.download(
            tickers=tickers,
            period=_LOOKBACK_PERIOD,
            group_by="ticker",
            auto_adjust=False,
            threads=True,
            progress=False,
        )
    except Exception as exc:  # noqa: BLE001
        logger.warning("Batch download failed (%d tickers): %s", len(tickers), exc)
        return []

    return _parse_download_batch(raw, tickers)


def fetch_market_data(
    tickers: list[str],
    *,
    batch_size: int = _DEFAULT_BATCH_SIZE,
) -> pd.DataFrame:
    """
    Fetch historical daily data for all tickers using batched downloads.

    Parameters
    ----------
    tickers:
        Yahoo Finance HK ticker strings (e.g. ``0700.HK``).
    batch_size:
        Number of symbols passed to each ``yf.download`` call.

    Returns
    -------
    pd.DataFrame
        Long-format master table with MultiIndex [Ticker, Date] and OHLCV columns.
        Empty when no ticker returned data.
    """
    if not tickers:
        logger.warning("No tickers supplied to fetch_market_data")
        return pd.DataFrame(columns=["Ticker", "Date", "Open", "High", "Low", "Close", "Volume"])

    frames: list[pd.DataFrame] = []
    batches = list(_chunked(tickers, batch_size))
    success_count = 0

    logger.info(
        "Starting batched fetch for %d tickers (%d batches of up to %d, period=%s)",
        len(tickers),
        len(batches),
        batch_size,
        _LOOKBACK_PERIOD,
    )

    for batch_index, batch in enumerate(batches, start=1):
        batch_frames = _download_batch(batch)
        frames.extend(batch_frames)
        success_count += len(batch_frames)
        failed_in_batch = len(batch) - len(batch_frames)

        logger.info(
            "Batch %d/%d: %d with data, %d empty (%d tickers in batch)",
            batch_index,
            len(batches),
            len(batch_frames),
            failed_in_batch,
            len(batch),
        )

    failed_count = len(tickers) - success_count
    logger.info(
        "Fetch complete: %d succeeded, %d empty/failed",
        success_count,
        failed_count,
    )

    if not frames:
        return pd.DataFrame(columns=["Ticker", "Date", "Open", "High", "Low", "Close", "Volume"])

    master = pd.concat(frames, ignore_index=True)
    master = master.sort_values(["Ticker", "Date"]).reset_index(drop=True)
    master = master.set_index(["Ticker", "Date"]).sort_index()

    logger.info(
        "Master DataFrame built: %d rows, %d unique tickers, %d unique dates",
        len(master),
        master.index.get_level_values("Ticker").nunique(),
        master.index.get_level_values("Date").nunique(),
    )
    return master


def fetch_market_caps(tickers: list[str]) -> dict[str, int | None]:
    """
    Fetch market capitalisation for a list of tickers via yfinance.

    Intended for alert tickers only to minimise API calls.
    """
    if not tickers:
        return {}

    caps: dict[str, int | None] = {}
    for ticker in tickers:
        try:
            info = yf.Ticker(ticker).fast_info
            cap = info.get("marketCap")
            if cap is None:
                cap = yf.Ticker(ticker).info.get("marketCap")
            caps[ticker] = int(cap) if cap is not None else None
        except Exception:  # noqa: BLE001
            caps[ticker] = None

    resolved = sum(1 for value in caps.values() if value is not None)
    logger.info(
        "Market cap fetch complete: %d/%d tickers resolved",
        resolved,
        len(tickers),
    )
    return caps
