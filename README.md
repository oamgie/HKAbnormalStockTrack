# HK Abnormal Stock Track

A stateless, end-of-day (EOD) volume screener for the Hong Kong Stock Exchange (HKEX). Each run discovers active HK listings, pulls recent daily data via [yfinance](https://github.com/ranaroussi/yfinance), and flags stocks whose trading volume shifted significantly versus the **prior trading session**.

No database is required — all data is fetched and processed in memory.

## Latest alerts

<!-- DAILY_ALERTS_START -->
<details>
<summary><strong>📊 Daily volume alerts — click to expand</strong></summary>

*Run the screener to populate this section with the latest HKEX volume anomalies.*

</details>
<!-- DAILY_ALERTS_END -->

## What it detects

A stock is included in the daily alert list when **all** of the following are true:

| Rule | Threshold |
|------|-----------|
| Volume change | ≥ **+20%** or ≤ **−20%** vs prior session |
| Liquidity floor | Latest session volume **> 100,000** shares |
| Valid prior session | Prior session volume > 0 (no divide-by-zero) |

`Pct_Change` is formatted with an explicit sign (e.g. `+83.91%`, `−30.26%`).

## How trading dates work

The screener does **not** use calendar “yesterday.” It inspects the fetched price history and picks the two most recent dates with positive volume across the market:

- **Monday run** → compares Monday vs Friday
- **After a holiday** → skips non-trading days automatically

`Date_Today` and `Date_Prev` in the output refer to those two **trading** sessions, not calendar dates.

Data is fetched with a **5-calendar-day** lookback so weekends and short gaps are covered. Very long market closures (e.g. extended holidays) may yield an empty report if fewer than two sessions appear in the window.

## Project structure

```
hkAbnormalStockTrack/
├── main.py                 # Pipeline orchestrator
├── ticker_provider.py      # HK ticker + name discovery (Sina, Wikipedia)
├── data_fetcher.py         # Batched yfinance downloads
├── screener.py             # Volume anomaly logic
├── readme_updater.py       # Collapsible daily alerts block for README.md
├── report_cleanup.py       # Deletes reports older than 30 days
├── reports/                # Daily CSV archives (committed by CI)
├── .github/workflows/
│   └── daily_run.yml       # Scheduled GitHub Actions job
└── requirements.txt
```

## Output

Each successful run produces:

| Output | Location | Description |
|--------|----------|-------------|
| CSV report | `reports/hk_volume_alerts_YYYYMMDD.csv` | Full alert list |
| Console table | stdout | Markdown-style table |
| GitHub summary | `github_summary.md` | Used by Actions for UI + email |
| README toggle | `README.md` | Collapsible daily alert table on the repo homepage |

### CSV columns

| Column | Description |
|--------|-------------|
| `Ticker` | Yahoo Finance symbol (e.g. `0700.HK`) |
| `Name` | English name |
| `Name_ZH` | Chinese name |
| `Date_Today` | Latest trading session in the dataset |
| `Date_Prev` | Prior trading session |
| `Volume_Today` | Shares traded on latest session |
| `Volume_Prev` | Shares traded on prior session |
| `Pct_Change` | Signed percent change (e.g. `+83.91%`) |

Reports older than **30 days** are deleted automatically on each run.

## Local setup

**Requirements:** Python 3.11+

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

A full run screens ~2,800 active HK tickers and typically takes **45–60 minutes** locally, depending on network speed and Yahoo rate limits.

## GitHub Actions automation

The workflow in `.github/workflows/daily_run.yml`:

1. Runs **Monday–Friday at 09:15 UTC** (17:15 HKT) — after the HK close, with time for EOD data to settle
2. Executes `python main.py`
3. Publishes a **GitHub Step Summary** from `github_summary.md`
4. Sends a **daily email** (when configured)
5. Commits updated/deleted files under `reports/` and refreshes the collapsible **Latest alerts** section in `README.md`

You can also trigger a run manually via **Actions → Daily HK Volume Screener → Run workflow**.

### Email secrets

Add these repository secrets under **Settings → Secrets and variables → Actions**:

| Secret | Example |
|--------|---------|
| `SMTP_SERVER` | `smtp.gmail.com` |
| `SMTP_USER` | Your sender email |
| `SMTP_PASS` | App password or SMTP credential |
| `RECEIVER_EMAIL` | Alert recipient |

**`SMTP_SERVER` must be hostname only** — no `https://`, no port, no trailing spaces.

| Provider | `SMTP_SERVER` value |
|----------|---------------------|
| Gmail | `smtp.gmail.com` |
| Outlook / Microsoft 365 | `smtp.office365.com` (often port **587** — see note below) |
| Yahoo | `smtp.mail.yahoo.com` |

Gmail uses port **465** (SSL), which matches this workflow. If you use Outlook/Office365, you may need port **587** with STARTTLS instead — say the word and we can adjust the workflow.

`SMTP_PASS` for Gmail must be a [Google App Password](https://myaccount.google.com/apppasswords), not your normal login password.

## Data sources

| Source | Used for |
|--------|----------|
| **Sina Finance** | Active HK ticker list, English + Chinese names |
| **Wikipedia** | Index constituent cross-check |
| **yfinance / Yahoo Finance** | Daily OHLCV history (free, may be delayed) |
| **East Money** | Optional ticker enrichment (best-effort) |

## Design principles

- **Stateless** — no database; each run is independent
- **Holiday-aware dates** — derived from actual volume data, not hardcoded offsets
- **Graceful degradation** — missing tickers, empty batches, and API failures are logged and skipped without crashing the pipeline
- **Free infrastructure** — yfinance + GitHub Actions free tier

## Disclaimer

Market data is pulled from free, public sources and may be subject to exchange delays, omissions, or inaccuracies. This tool is for informational purposes only and is not investment advice.
