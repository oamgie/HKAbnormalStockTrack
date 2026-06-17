#!/usr/bin/env python3
"""
Stateless EOD HKEX volume screener.

Discovers HK tickers, fetches recent daily data via yfinance, screens for
significant day-over-day volume changes, and writes results to console + CSV.
"""

from __future__ import annotations

import logging
import sys
import time
from datetime import datetime
from pathlib import Path

import pandas as pd
from tabulate import tabulate

from data_fetcher import fetch_market_data
from report_cleanup import prune_old_reports
from screener import _resolve_latest_trading_dates, screen_volume_changes
from ticker_provider import get_hk_tickers

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger("hk_volume_screener")

# yfinance logs every missing/delisted symbol at ERROR; suppress that noise.
logging.getLogger("yfinance").setLevel(logging.CRITICAL)

REPORTS_DIR = Path(__file__).resolve().parent / "reports"


def _format_pct_change(value: float | int) -> str:
    """Format percent change with an explicit sign and percent suffix."""
    return f"{float(value):+.2f}%"


def _attach_stock_names(
    df: pd.DataFrame,
    english_names: dict[str, str],
    chinese_names: dict[str, str],
) -> pd.DataFrame:
    """Add English and Chinese name columns after Ticker."""
    if df.empty:
        return df

    enriched = df.copy()
    enriched.insert(1, "Name", enriched["Ticker"].map(english_names).fillna(""))
    enriched.insert(2, "Name_ZH", enriched["Ticker"].map(chinese_names).fillna(""))
    return enriched


def _format_results_table(df: pd.DataFrame) -> str:
    """Render screener output as a GitHub-flavoured markdown table."""
    if df.empty:
        return "_No volume alerts met the screening criteria today._"

    display = df.copy()
    for date_col in ("Date_Today", "Date_Prev"):
        if date_col in display.columns:
            display[date_col] = pd.to_datetime(display[date_col]).dt.strftime("%Y-%m-%d")
    display["Volume_Today"] = display["Volume_Today"].map(lambda v: f"{v:,}")
    display["Volume_Prev"] = display["Volume_Prev"].map(lambda v: f"{v:,}")
    display["Pct_Change"] = display["Pct_Change"].map(_format_pct_change)

    return tabulate(display, headers="keys", tablefmt="github", showindex=False)


def _save_report(df: pd.DataFrame, run_date: datetime) -> Path:
    """Persist screened results to reports/hk_volume_alerts_YYYYMMDD.csv."""
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    filename = f"hk_volume_alerts_{run_date.strftime('%Y%m%d')}.csv"
    output_path = REPORTS_DIR / filename

    export = df.copy()
    if not export.empty:
        for date_col in ("Date_Today", "Date_Prev"):
            export[date_col] = pd.to_datetime(export[date_col]).dt.strftime("%Y-%m-%d")
        export["Pct_Change"] = export["Pct_Change"].map(_format_pct_change)

    export.to_csv(output_path, index=False)
    logger.info("Report saved to %s", output_path)
    return output_path


def generate_github_markdown_summary(
    df: pd.DataFrame,
    date_today: str,
    date_prev: str,
) -> None:
    """
    Surgically converts the existing finalized filtered DataFrame into a Markdown
    report artifact without altering the core calculation matrices.
    """
    execution_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if not df.empty:
        # Clone df to preserve raw types in any other simultaneous output components
        display_df = df.copy()

        # Ensure direction emojis visually anchors the UI trends
        if "Pct_Change" in display_df.columns:
            display_df["Direction"] = display_df["Pct_Change"].apply(
                lambda x: "📈 UP" if x >= 0 else "📉 DOWN"
            )
            display_df["Pct_Change"] = display_df["Pct_Change"].apply(
                lambda x: _format_pct_change(x) if isinstance(x, (int, float)) else str(x)
            )

        if "Volume_Today" in display_df.columns:
            display_df["Volume_Today"] = display_df["Volume_Today"].apply(
                lambda x: f"{x:,.0f}" if isinstance(x, (int, float)) else str(x)
            )

        if "Volume_Prev" in display_df.columns:
            display_df["Volume_Prev"] = display_df["Volume_Prev"].apply(
                lambda x: f"{x:,.0f}" if isinstance(x, (int, float)) else str(x)
            )

        for date_col in ("Date_Today", "Date_Prev"):
            if date_col in display_df.columns:
                display_df[date_col] = pd.to_datetime(display_df[date_col]).dt.strftime(
                    "%Y-%m-%d"
                )

        table_content = display_df.to_markdown(index=False)
    else:
        table_content = "\n*No stocks met the volume anomaly criteria for today.*"

    markdown_text = f"""### 📊 HKEX EOD Volume Anomalies Alert
> **Latest Session:** {date_today} | **Prior Session:** {date_prev} | **Analysis Executed At:** {execution_time} HKT
> *Filters Applied: Volume Change ≥ +20% or ≤ -20% | Minimum Volume Floor: > 100,000 shares.*

{table_content}

---
*⚠️ Disclaimer: Market data is pulled from free, public streams and may be subject to standard exchange delays.*
"""

    with open("github_summary.md", "w", encoding="utf-8") as summary_file:
        summary_file.write(markdown_text)


def run() -> int:
    """Execute the full discovery → fetch → screen pipeline."""
    pipeline_start = time.perf_counter()
    run_date = datetime.now()

    logger.info("=" * 60)
    logger.info("HKEX EOD Volume Screener — run started")
    logger.info("=" * 60)

    # Phase 1: Ticker discovery
    phase_start = time.perf_counter()
    try:
        tickers, english_names, chinese_names = get_hk_tickers()
    except Exception as exc:  # noqa: BLE001
        logger.exception("Ticker discovery failed: %s", exc)
        return 1

    logger.info(
        "Phase 1 complete — %d tickers discovered (%.2fs)",
        len(tickers),
        time.perf_counter() - phase_start,
    )

    if not tickers:
        logger.error("No tickers available; aborting")
        return 1

    # Phase 2: Concurrent data fetch
    phase_start = time.perf_counter()
    try:
        market_data = fetch_market_data(tickers)
    except Exception as exc:  # noqa: BLE001
        logger.exception("Data fetch failed: %s", exc)
        return 1

    logger.info(
        "Phase 2 complete — master DataFrame shape %s (%.2fs)",
        market_data.shape,
        time.perf_counter() - phase_start,
    )

    if market_data.empty:
        logger.error("No market data retrieved; aborting")
        return 1

    # Phase 3: Volume screening
    phase_start = time.perf_counter()
    try:
        alerts = screen_volume_changes(market_data)
    except Exception as exc:  # noqa: BLE001
        logger.exception("Screening failed: %s", exc)
        return 1

    logger.info(
        "Phase 3 complete — %d alerts found (%.2fs)",
        len(alerts),
        time.perf_counter() - phase_start,
    )

    alerts = _attach_stock_names(alerts, english_names, chinese_names)

    # Phase 4: Output
    print("\n## HKEX EOD Volume Alerts\n")
    print(_format_results_table(alerts))
    print()

    _save_report(alerts, run_date)
    prune_old_reports(REPORTS_DIR)

    date_today, date_prev = _resolve_latest_trading_dates(market_data)
    generate_github_markdown_summary(
        alerts,
        date_today.strftime("%Y-%m-%d"),
        date_prev.strftime("%Y-%m-%d"),
    )
    logger.info("GitHub summary written to github_summary.md")

    elapsed = time.perf_counter() - pipeline_start
    logger.info("Pipeline finished in %.2fs", elapsed)
    return 0


if __name__ == "__main__":
    sys.exit(run())
