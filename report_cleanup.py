"""
Retention policy for generated daily XLSX reports.
"""

from __future__ import annotations

import logging
import re
from datetime import datetime, timedelta
from pathlib import Path

logger = logging.getLogger(__name__)

_REPORT_FILENAME_PATTERN = re.compile(r"^hk_volume_alerts_(\d{8})\.xlsx$")
_DEFAULT_RETENTION_DAYS = 30


def prune_old_reports(
    reports_dir: Path,
    *,
    retention_days: int = _DEFAULT_RETENTION_DAYS,
    reference_date: datetime | None = None,
) -> list[Path]:
    """
    Delete report XLSX files older than ``retention_days`` from ``reports_dir``.

    Filenames must match ``hk_volume_alerts_YYYYMMDD.xlsx``.
    """
    if retention_days < 1:
        raise ValueError("retention_days must be at least 1")

    if not reports_dir.exists():
        logger.info("Reports directory does not exist; nothing to prune")
        return []

    cutoff = (reference_date or datetime.now()) - timedelta(days=retention_days)
    removed: list[Path] = []

    for report_path in sorted(reports_dir.glob("hk_volume_alerts_*.xlsx")):
        match = _REPORT_FILENAME_PATTERN.match(report_path.name)
        if not match:
            continue

        try:
            report_date = datetime.strptime(match.group(1), "%Y%m%d")
        except ValueError:
            logger.warning("Skipping report with unparseable date: %s", report_path.name)
            continue

        if report_date < cutoff:
            report_path.unlink()
            removed.append(report_path)
            logger.info("Deleted old report: %s", report_path.name)

    if removed:
        logger.info(
            "Pruned %d report(s) older than %d days (cutoff %s)",
            len(removed),
            retention_days,
            cutoff.strftime("%Y-%m-%d"),
        )
    else:
        logger.info("No reports older than %d days to prune", retention_days)

    return removed
