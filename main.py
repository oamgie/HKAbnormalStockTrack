#!/usr/bin/env python3
"""
Stateless EOD HKEX trading-value screener.

Discovers HK tickers, fetches recent daily data via yfinance, screens for
significant day-over-day turnover changes, and writes results to console + XLSX.
"""

from __future__ import annotations

import logging
import sys
import time
from datetime import datetime
from pathlib import Path

import pandas as pd
from tabulate import tabulate

from data_fetcher import fetch_market_caps, fetch_market_data
from readme_updater import update_readme_daily_alerts
from report_cleanup import prune_old_reports
from screener import _resolve_latest_trading_dates, screen_value_changes
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
README_PATH = Path(__file__).resolve().parent / "README.md"
ATTACHMENT_HINT_PATH = Path(__file__).resolve().parent / "report_attachment.txt"

_EXPORT_COLUMNS = [
    "Ticker",
    "Name",
    "Name_ZH",
    "Date_Today",
    "Date_Prev",
    "Volume_Today",
    "Volume_Prev",
    "Close_Today",
    "Price_Pct_Change",
    "Value_Pct_Change",
    "Market_Cap",
]


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


def _attach_market_caps(df: pd.DataFrame, market_caps: dict[str, int | None]) -> pd.DataFrame:
    """Add Market_Cap column from a ticker → cap mapping."""
    if df.empty:
        return df

    enriched = df.copy()
    enriched["Market_Cap"] = enriched["Ticker"].map(market_caps)
    return enriched


def _order_export_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Return DataFrame with standard export column order."""
    if df.empty:
        return pd.DataFrame(columns=_EXPORT_COLUMNS)
    present = [col for col in _EXPORT_COLUMNS if col in df.columns]
    return df[present].copy()


def _format_results_table(df: pd.DataFrame) -> str:
    """Render screener output as a GitHub-flavoured markdown table."""
    if df.empty:
        return "_No value alerts met the screening criteria today._"

    display = _order_export_columns(df).copy()
    for date_col in ("Date_Today", "Date_Prev"):
        if date_col in display.columns:
            display[date_col] = pd.to_datetime(display[date_col]).dt.strftime("%Y-%m-%d")
    for volume_col in ("Volume_Today", "Volume_Prev"):
        if volume_col in display.columns:
            display[volume_col] = display[volume_col].map(lambda v: f"{v:,}")
    if "Close_Today" in display.columns:
        display["Close_Today"] = display["Close_Today"].map(lambda v: f"{v:.3f}")
    for pct_col in ("Price_Pct_Change", "Value_Pct_Change"):
        if pct_col in display.columns:
            display[pct_col] = display[pct_col].map(_format_pct_change)
    if "Market_Cap" in display.columns:
        display["Market_Cap"] = display["Market_Cap"].map(
            lambda v: f"{int(v):,}" if pd.notna(v) else ""
        )

    return tabulate(display, headers="keys", tablefmt="github", showindex=False)


def _save_report(df: pd.DataFrame, run_date: datetime) -> Path:
    """Persist screened results to reports/hk_volume_alerts_YYYYMMDD.xlsx."""
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    filename = f"hk_volume_alerts_{run_date.strftime('%Y%m%d')}.xlsx"
    output_path = REPORTS_DIR / filename

    export = _order_export_columns(df).copy()
    if not export.empty:
        for date_col in ("Date_Today", "Date_Prev"):
            export[date_col] = pd.to_datetime(export[date_col]).dt.strftime("%Y-%m-%d")
        for pct_col in ("Price_Pct_Change", "Value_Pct_Change"):
            export[pct_col] = export[pct_col].map(_format_pct_change)
        export["Volume_Today"] = export["Volume_Today"].astype("Int64")
        export["Volume_Prev"] = export["Volume_Prev"].astype("Int64")
        export["Close_Today"] = export["Close_Today"].round(3)
        if "Market_Cap" in export.columns:
            export["Market_Cap"] = export["Market_Cap"].astype("Int64")

    export.to_excel(output_path, index=False, engine="openpyxl")
    ATTACHMENT_HINT_PATH.write_text(f"reports/{filename}", encoding="utf-8")
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
        display_df = _order_export_columns(df).copy()

        if "Value_Pct_Change" in display_df.columns:
            display_df["Direction"] = display_df["Value_Pct_Change"].apply(
                lambda x: "📈 UP" if x >= 0 else "📉 DOWN"
            )
            display_df["Value_Pct_Change"] = display_df["Value_Pct_Change"].apply(
                lambda x: _format_pct_change(x) if isinstance(x, (int, float)) else str(x)
            )

        if "Price_Pct_Change" in display_df.columns:
            display_df["Price_Pct_Change"] = display_df["Price_Pct_Change"].apply(
                lambda x: _format_pct_change(x) if isinstance(x, (int, float)) else str(x)
            )

        for volume_col in ("Volume_Today", "Volume_Prev"):
            if volume_col in display_df.columns:
                display_df[volume_col] = display_df[volume_col].apply(
                    lambda x: f"{x:,.0f}" if isinstance(x, (int, float)) else str(x)
                )

        if "Close_Today" in display_df.columns:
            display_df["Close_Today"] = display_df["Close_Today"].apply(
                lambda x: f"{x:.3f}" if isinstance(x, (int, float)) else str(x)
            )

        if "Market_Cap" in display_df.columns:
            display_df["Market_Cap"] = display_df["Market_Cap"].apply(
                lambda x: f"{int(x):,}" if pd.notna(x) and isinstance(x, (int, float)) else ""
            )

        for date_col in ("Date_Today", "Date_Prev"):
            if date_col in display_df.columns:
                display_df[date_col] = pd.to_datetime(display_df[date_col]).dt.strftime(
                    "%Y-%m-%d"
                )

        table_content = display_df.to_markdown(index=False)
    else:
        table_content = "\n*No stocks met the trading value anomaly criteria for today.*"

    markdown_text = f"""### 📊 HKEX EOD Trading Value Anomalies Alert
> **Latest Session:** {date_today} | **Prior Session:** {date_prev} | **Analysis Executed At:** {execution_time} HKT
> *Filters Applied: Turnover Change ≥ +20% or ≤ -20% | Minimum Turnover Floor: > HKD 15,000,000.*

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
    logger.info("HKEX EOD Trading Value Screener — run started")
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

    # Phase 3: Value screening
    phase_start = time.perf_counter()
    try:
        alerts = screen_value_changes(market_data)
    except Exception as exc:  # noqa: BLE001
        logger.exception("Screening failed: %s", exc)
        return 1

    logger.info(
        "Phase 3 complete — %d alerts found (%.2fs)",
        len(alerts),
        time.perf_counter() - phase_start,
    )

    alerts = _attach_stock_names(alerts, english_names, chinese_names)

    if not alerts.empty:
        phase_start = time.perf_counter()
        market_caps = fetch_market_caps(alerts["Ticker"].tolist())
        alerts = _attach_market_caps(alerts, market_caps)
        logger.info(
            "Market cap enrichment complete (%.2fs)",
            time.perf_counter() - phase_start,
        )

    # Phase 4: Output
    print("\n## HKEX EOD Trading Value Alerts\n")
    print(_format_results_table(alerts))
    print()

    _save_report(alerts, run_date)
    prune_old_reports(REPORTS_DIR)

    date_today, date_prev = _resolve_latest_trading_dates(market_data)
    date_today_str = date_today.strftime("%Y-%m-%d")
    date_prev_str = date_prev.strftime("%Y-%m-%d")
    report_filename = f"hk_volume_alerts_{run_date.strftime('%Y%m%d')}.xlsx"

    generate_github_markdown_summary(alerts, date_today_str, date_prev_str)
    logger.info("GitHub summary written to github_summary.md")

    try:
        update_readme_daily_alerts(
            alerts,
            readme_path=README_PATH,
            date_today=date_today_str,
            date_prev=date_prev_str,
            report_filename=report_filename,
            updated_at=run_date,
        )
    except Exception as exc:  # noqa: BLE001
        logger.warning("README update failed (non-fatal): %s", exc)

    elapsed = time.perf_counter() - pipeline_start
    logger.info("Pipeline finished in %.2fs", elapsed)
    return 0


if __name__ == "__main__":
    sys.exit(run())
