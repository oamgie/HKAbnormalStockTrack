"""
HKEX ticker discovery for Yahoo Finance.

Yahoo Finance uses 4-digit zero-padded codes with a .HK suffix (e.g. 0700.HK).
We assemble the universe from currently listed HK equities (Sina Finance API,
with optional East Money enrichment) plus Wikipedia index constituents.
"""

from __future__ import annotations

import json
import logging
import re
import time
from http.client import RemoteDisconnected
from io import StringIO
from typing import Iterable
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

import pandas as pd

logger = logging.getLogger(__name__)

# Wikipedia pages that list liquid, actively traded HK index constituents.
_WIKIPEDIA_INDEX_PAGES = [
    "https://en.wikipedia.org/wiki/Hang_Seng_Index",
    "https://en.wikipedia.org/wiki/Hang_Seng_China_Enterprises_Index",
    "https://en.wikipedia.org/wiki/Hang_Seng_Composite_Index",
]

# Sina Finance HK full-market screener (reliable, paginated JSON API).
_SINA_HK_API = (
    "https://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/"
    "Market_Center.getHKStockData"
)
_SINA_PAGE_SIZE = 60
_SINA_PAGE_DELAY_SEC = 0.15
_SINA_MAX_PAGES = 80

# East Money market filter: HK main board + GEM listed equities (best-effort).
_EASTMONEY_HOSTS = ("63.push2.eastmoney.com", "72.push2.eastmoney.com", "push2.eastmoney.com")
_EASTMONEY_HK_FS = "m:128+t:3,m:128+t:4,m:128+t:1,m:128+t:2"
_EASTMONEY_PAGE_SIZE = 100
_EASTMONEY_PAGE_DELAY_SEC = 0.75
_EASTMONEY_MAX_RETRIES = 4

_USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)
_SINA_REFERER = "https://finance.sina.com.cn/"
_EASTMONEY_REFERER = "https://quote.eastmoney.com/center/gridlist.html"


def _normalize_hk_code(raw: str) -> str | None:
    """Convert assorted code formats to Yahoo-style tickers (e.g. 0700.HK)."""
    if raw is None or (isinstance(raw, float) and pd.isna(raw)):
        return None

    text = str(raw).strip().upper()
    if not text:
        return None

    if re.fullmatch(r"\d{4}\.HK", text):
        return text

    text = re.sub(r"\.HK$", "", text)
    text = re.sub(r"^HK", "", text)

    digits = re.sub(r"\D", "", text)
    if not digits:
        return None

    code = int(digits)
    if code < 1 or code > 9999:
        return None

    return f"{code:04d}.HK"


def _pick_english_name(item: dict, *, eng_key: str = "engname") -> str:
    """Extract the English display name when available."""
    return str(item.get(eng_key, "")).strip()


def _pick_chinese_name(item: dict, *, local_key: str = "name") -> str:
    """Extract the Chinese display name when available."""
    return str(item.get(local_key, "")).strip()


def _fetch_wikipedia_tables(url: str) -> list[pd.DataFrame]:
    """Download and parse HTML tables from a Wikipedia page."""
    request = Request(url, headers={"User-Agent": _USER_AGENT})
    with urlopen(request, timeout=30) as response:
        html = response.read().decode("utf-8", errors="replace")
    return pd.read_html(StringIO(html))


def _extract_codes_from_tables(tables: Iterable[pd.DataFrame]) -> set[str]:
    """Pull HK stock codes from Wikipedia index constituent tables."""
    codes: set[str] = set()
    code_column_hints = ("code", "ticker", "symbol", "stock code", "hk")

    for table in tables:
        if table.empty:
            continue

        normalized_columns = {str(col).strip().lower(): col for col in table.columns}

        candidate_columns: list = []
        for hint in code_column_hints:
            for norm, original in normalized_columns.items():
                if hint in norm:
                    candidate_columns.append(original)

        if not candidate_columns:
            candidate_columns = list(table.columns)

        for column in candidate_columns:
            for value in table[column].dropna().astype(str):
                ticker = _normalize_hk_code(value)
                if ticker:
                    codes.add(ticker)

    return codes


def _scrape_index_constituents() -> set[str]:
    """Scrape HK index constituents from Wikipedia as a verified active set."""
    codes: set[str] = set()

    for url in _WIKIPEDIA_INDEX_PAGES:
        try:
            tables = _fetch_wikipedia_tables(url)
            page_codes = _extract_codes_from_tables(tables)
            logger.info(
                "Scraped %d tickers from %s",
                len(page_codes),
                url.rsplit("/", maxsplit=1)[-1].replace("_", " "),
            )
            codes.update(page_codes)
        except (URLError, ValueError, pd.errors.ParserError) as exc:
            logger.warning("Failed to scrape %s: %s", url, exc)

    return codes


def _fetch_sina_page(page: int) -> list[dict]:
    """Fetch one page of the Sina Finance HK equity list."""
    params = urlencode(
        {
            "page": page,
            "num": _SINA_PAGE_SIZE,
            "sort": "symbol",
            "asc": 1,
            "node": "qbgg_hk",
            "_s_r_a": "page",
        }
    )
    url = f"{_SINA_HK_API}?{params}"
    request = Request(
        url,
        headers={"User-Agent": _USER_AGENT, "Referer": _SINA_REFERER},
    )
    with urlopen(request, timeout=30) as response:
        payload = json.loads(response.read())

    if not isinstance(payload, list):
        return []
    return payload


def _fetch_sina_hk_equities() -> tuple[dict[str, str], dict[str, str]]:
    """
    Download currently listed HK equity codes and names from Sina Finance.

    Primary listed-ticker source; stable compared to East Money push endpoints.
    Returns separate English and Chinese name lookups.
    """
    english_names: dict[str, str] = {}
    chinese_names: dict[str, str] = {}

    for page in range(1, _SINA_MAX_PAGES + 1):
        if page > 1:
            time.sleep(_SINA_PAGE_DELAY_SEC)

        try:
            items = _fetch_sina_page(page)
        except (URLError, TimeoutError, json.JSONDecodeError, RemoteDisconnected) as exc:
            logger.warning("Sina page %d failed: %s", page, exc)
            if english_names or chinese_names:
                logger.warning(
                    "Returning %d tickers collected before Sina pagination stopped",
                    len(english_names | chinese_names.keys()),
                )
                break
            raise

        if not items:
            break

        for item in items:
            ticker = _normalize_hk_code(str(item.get("symbol", "")))
            if not ticker:
                continue
            english = _pick_english_name(item)
            chinese = _pick_chinese_name(item)
            if english:
                english_names[ticker] = english
            else:
                english_names.setdefault(ticker, "")
            if chinese:
                chinese_names[ticker] = chinese
            else:
                chinese_names.setdefault(ticker, "")

        if len(items) < _SINA_PAGE_SIZE:
            break

    logger.info("Fetched %d listed HK tickers from Sina Finance", len(english_names))
    return english_names, chinese_names


def _fetch_eastmoney_page(page: int, host: str) -> dict:
    """Fetch one page of the East Money HK equity screener API from a given host."""
    params = urlencode(
        {
            "pn": page,
            "pz": _EASTMONEY_PAGE_SIZE,
            "po": 1,
            "np": 1,
            "fltt": 2,
            "invt": 2,
            "fid": "f3",
            "fs": _EASTMONEY_HK_FS,
            "fields": "f12,f14",
        }
    )
    url = f"https://{host}/api/qt/clist/get?{params}"
    request = Request(
        url,
        headers={"User-Agent": _USER_AGENT, "Referer": _EASTMONEY_REFERER},
    )

    with urlopen(request, timeout=30) as response:
        return json.loads(response.read())


def _fetch_eastmoney_page_with_retries(page: int) -> dict | None:
    """Try multiple East Money hosts with exponential backoff."""
    last_error: Exception | None = None

    for host in _EASTMONEY_HOSTS:
        for attempt in range(1, _EASTMONEY_MAX_RETRIES + 1):
            try:
                return _fetch_eastmoney_page(page, host)
            except (
                URLError,
                HTTPError,
                TimeoutError,
                json.JSONDecodeError,
                RemoteDisconnected,
                ConnectionResetError,
                OSError,
            ) as exc:
                last_error = exc
                delay = 0.5 * attempt
                logger.debug(
                    "East Money page %d via %s attempt %d failed: %s",
                    page,
                    host,
                    attempt,
                    exc,
                )
                time.sleep(delay)

    logger.warning("East Money page %d unavailable after retries: %s", page, last_error)
    return None


def _fetch_eastmoney_hk_equities() -> tuple[dict[str, str], dict[str, str]]:
    """
    Best-effort download of HK equity codes and names from East Money.

    Returns partial results when later pages fail; returns empty dicts when the
    first page cannot be retrieved. East Money ``f14`` is treated as Chinese.
    """
    english_names: dict[str, str] = {}
    chinese_names: dict[str, str] = {}
    page = 1
    total_expected: int | None = None

    while page <= _SINA_MAX_PAGES:
        if page > 1:
            time.sleep(_EASTMONEY_PAGE_DELAY_SEC)

        payload = _fetch_eastmoney_page_with_retries(page)
        if payload is None:
            if english_names or chinese_names:
                logger.warning(
                    "East Money stopped at page %d; keeping %d tickers collected so far",
                    page,
                    len(english_names | chinese_names.keys()),
                )
            break

        data = payload.get("data") or {}
        items = data.get("diff") or []

        if total_expected is None:
            total_expected = int(data.get("total") or 0)
            if total_expected:
                logger.info("East Money reports %d listed HK equities", total_expected)

        if not items:
            break

        for item in items:
            ticker = _normalize_hk_code(str(item.get("f12", "")))
            if not ticker:
                continue
            chinese = str(item.get("f14", "")).strip()
            english_names.setdefault(ticker, "")
            if chinese and (ticker not in chinese_names or not chinese_names[ticker]):
                chinese_names[ticker] = chinese
            else:
                chinese_names.setdefault(ticker, "")

        if total_expected and len(english_names | chinese_names.keys()) >= total_expected:
            break
        if len(items) < _EASTMONEY_PAGE_SIZE:
            break

        page += 1

    if english_names or chinese_names:
        logger.info(
            "Fetched %d listed HK tickers from East Money (%d pages)",
            len(english_names | chinese_names.keys()),
            page,
        )

    return english_names, chinese_names


def _merge_name_lookup(
    primary: dict[str, str],
    secondary: dict[str, str],
) -> dict[str, str]:
    """Merge name maps, keeping existing non-empty values in ``primary``."""
    merged = dict(primary)
    for ticker, name in secondary.items():
        if ticker not in merged:
            merged[ticker] = name
        elif name and not merged[ticker]:
            merged[ticker] = name
        merged.setdefault(ticker, "")
    return merged


def get_hk_tickers() -> tuple[list[str], dict[str, str], dict[str, str]]:
    """
    Return a sorted ticker list plus English and Chinese name lookups.

    Strategy:
    1. Sina Finance — primary listed-equity source (stable JSON API).
    2. East Money — optional enrichment when reachable.
    3. Wikipedia index constituents — redundancy for liquid large caps.
    """
    english_names: dict[str, str] = {}
    chinese_names: dict[str, str] = {}

    try:
        sina_english, sina_chinese = _fetch_sina_hk_equities()
        english_names = _merge_name_lookup(english_names, sina_english)
        chinese_names = _merge_name_lookup(chinese_names, sina_chinese)
    except (URLError, TimeoutError, json.JSONDecodeError, RemoteDisconnected) as exc:
        logger.warning("Sina Finance ticker fetch failed: %s", exc)

    try:
        em_english, em_chinese = _fetch_eastmoney_hk_equities()
        english_names = _merge_name_lookup(english_names, em_english)
        chinese_names = _merge_name_lookup(chinese_names, em_chinese)
    except (URLError, TimeoutError, json.JSONDecodeError, RemoteDisconnected) as exc:
        logger.warning("East Money ticker fetch failed: %s", exc)

    scraped = _scrape_index_constituents()
    for ticker in scraped:
        english_names.setdefault(ticker, "")
        chinese_names.setdefault(ticker, "")

    tickers = sorted(english_names | chinese_names.keys() | scraped)
    if not tickers:
        raise RuntimeError(
            "Ticker discovery failed: no symbols returned from Sina, East Money, or Wikipedia"
        )

    named_count = sum(
        1 for ticker in tickers if english_names.get(ticker) or chinese_names.get(ticker)
    )
    logger.info(
        "Ticker universe ready: %d total (%d with names, %d from indices)",
        len(tickers),
        named_count,
        len(scraped),
    )
    return tickers, english_names, chinese_names
