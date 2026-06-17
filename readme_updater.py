"""
Inject the latest daily alert table into README.md inside a collapsible block.

GitHub renders HTML <details>/<summary> in README files, so the alert list
stays hidden until the user expands the toggle on the repository homepage.
"""

from __future__ import annotations

import logging
import re
from datetime import datetime
from pathlib import Path

import pandas as pd
from tabulate import tabulate

logger = logging.getLogger(__name__)

_START_MARKER = "<!-- DAILY_ALERTS_START -->"
_END_MARKER = "<!-- DAILY_ALERTS_END -->"

_DISPLAY_COLUMNS = [
    "Ticker",
    "Name",
    "Name_ZH",
    "Date_Today",
    "Date_Prev",
    "Volume_Today",
    "Close_Today",
    "Price_Pct_Change",
    "Value_Pct_Change",
    "Market_Cap",
]


def _format_pct_change(value: float | int | str) -> str:
    if isinstance(value, str) and value.endswith("%"):
        return value
    return f"{float(value):+.2f}%"


def _build_alerts_table(df: pd.DataFrame) -> str:
    """Render alerts as a GitHub-flavoured markdown table."""
    if df.empty:
        return "*No stocks met the trading value anomaly criteria for the latest session.*"

    display = df.copy()
    present = [col for col in _DISPLAY_COLUMNS if col in display.columns]
    display = display[present]

    for date_col in ("Date_Today", "Date_Prev"):
        if date_col in display.columns:
            display[date_col] = pd.to_datetime(display[date_col]).dt.strftime("%Y-%m-%d")
    for volume_col in ("Volume_Today", "Volume_Prev"):
        if volume_col in display.columns:
            display[volume_col] = display[volume_col].map(
                lambda value: f"{int(value):,}" if pd.notna(value) else ""
            )
    if "Close_Today" in display.columns:
        display["Close_Today"] = display["Close_Today"].map(
            lambda value: f"{float(value):.3f}" if pd.notna(value) else ""
        )
    for pct_col in ("Price_Pct_Change", "Value_Pct_Change"):
        if pct_col in display.columns:
            display[pct_col] = display[pct_col].map(_format_pct_change)
    if "Market_Cap" in display.columns:
        display["Market_Cap"] = display["Market_Cap"].map(
            lambda value: f"{int(value):,}" if pd.notna(value) else ""
        )

    return tabulate(display, headers="keys", tablefmt="github", showindex=False)


def build_daily_alerts_section(
    df: pd.DataFrame,
    *,
    date_today: str,
    date_prev: str,
    report_filename: str,
    updated_at: datetime | None = None,
) -> str:
    """Build the collapsible README block for the latest screening results."""
    timestamp = (updated_at or datetime.now()).strftime("%Y-%m-%d %H:%M:%S HKT")
    alert_count = len(df)
    summary_label = (
        f"📊 Daily trading value alerts — {alert_count} stocks "
        f"({date_today} vs {date_prev}) · click to expand"
    )
    table = _build_alerts_table(df)
    report_link = f"reports/{report_filename}"

    return f"""{_START_MARKER}
<details>
<summary><strong>{summary_label}</strong></summary>

> **Latest session:** {date_today} · **Prior session:** {date_prev} · **Updated:** {timestamp}  
> Filters: turnover change ≥ +20% or ≤ −20% · minimum turnover &gt; HKD 15,000,000

{table}

[Download full XLSX report]({report_link})

</details>
{_END_MARKER}
"""


def update_readme_daily_alerts(
    df: pd.DataFrame,
    *,
    readme_path: Path,
    date_today: str,
    date_prev: str,
    report_filename: str,
    updated_at: datetime | None = None,
) -> None:
    """
    Replace the daily alerts section in ``readme_path`` with fresh results.

    If markers are missing, the section is appended after the opening paragraph.
    """
    section = build_daily_alerts_section(
        df,
        date_today=date_today,
        date_prev=date_prev,
        report_filename=report_filename,
        updated_at=updated_at,
    )

    if not readme_path.exists():
        raise FileNotFoundError(f"README not found: {readme_path}")

    readme_text = readme_path.read_text(encoding="utf-8")
    pattern = re.compile(
        rf"{re.escape(_START_MARKER)}.*?{re.escape(_END_MARKER)}",
        flags=re.DOTALL,
    )

    if pattern.search(readme_text):
        updated = pattern.sub(section.strip(), readme_text, count=1)
    else:
        # First run: insert after the introductory paragraph when markers are absent.
        insertion_point = readme_text.find("\n\n## What it detects")
        if insertion_point == -1:
            updated = f"{readme_text.rstrip()}\n\n{section}\n"
        else:
            updated = f"{readme_text[:insertion_point]}\n\n{section}\n{readme_text[insertion_point:]}"

    readme_path.write_text(updated if updated.endswith("\n") else f"{updated}\n", encoding="utf-8")
    logger.info("README daily alerts section updated (%d alerts)", len(df))
