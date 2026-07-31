# HK Abnormal Stock Track

A stateless, end-of-day (EOD) trading-value screener for the Hong Kong Stock Exchange (HKEX). Each run discovers active HK listings, pulls recent daily data via [yfinance](https://github.com/ranaroussi/yfinance), and flags stocks whose turnover (Close × Volume) shifted significantly versus the **prior trading session**.

No database is required — all data is fetched and processed in memory.

## Latest alerts

<!-- DAILY_ALERTS_START -->
<details>
<summary><strong>📊 Daily trading value alerts — 61 stocks (2026-07-31 vs 2026-07-30) · click to expand</strong></summary>

> **Latest session:** 2026-07-31 · **Prior session:** 2026-07-30 · **Updated:** 2026-07-31 11:34:46 HKT  
> Filters: turnover change ≥ +20% or ≤ −20% · minimum turnover &gt; HKD 15,000,000

| Ticker   | Name   | Name_ZH   | Date_Today   | Date_Prev   | Turnover_Pct_Change   |   Turnover_Today |   Turnover_Prev |   Close_Today | Price_Pct_Change   |   Volume_Today |   Volume_Prev |        Market_Cap |
|----------|--------|-----------|--------------|-------------|-----------------------|------------------|-----------------|---------------|--------------------|----------------|---------------|-------------------|
| 2688.HK  |        |           | 2026-07-31   | 2026-07-30  | +130.17%              |      750,881,086 |     326,226,656 |         46.94 | +0.95%             |     15,996,615 |     7,015,627 |    52,190,456,401 |
| 1997.HK  |        |           | 2026-07-31   | 2026-07-30  | +127.92%              |      204,553,672 |      89,748,000 |         26.58 | +0.83%             |      7,695,774 |     3,404,704 |    80,702,922,120 |
| 6880.HK  |        |           | 2026-07-31   | 2026-07-30  | +121.56%              |       84,806,980 |      38,276,810 |        263    | -9.31%             |        322,460 |       131,989 |    61,946,496,893 |
| 0101.HK  |        |           | 2026-07-31   | 2026-07-30  | +116.77%              |      164,468,231 |      75,870,933 |          7.29 | -3.44%             |     22,560,800 |    10,049,130 |    37,930,471,430 |
| 9988.HK  |        |           | 2026-07-31   | 2026-07-30  | +103.69%              |   16,926,262,119 |   8,309,754,467 |        117    | +4.65%             |    144,668,907 |    74,326,961 | 2,243,472,408,918 |
| 0384.HK  |        |           | 2026-07-31   | 2026-07-30  | +87.14%               |      128,664,145 |      68,753,162 |          6.11 | -3.02%             |     21,057,961 |    10,913,200 |    33,288,213,974 |
| 0285.HK  |        |           | 2026-07-31   | 2026-07-30  | +86.07%               |      467,604,731 |     251,306,613 |         23.48 | -2.25%             |     19,915,023 |    10,462,390 |    52,738,626,551 |
| 0016.HK  |        |           | 2026-07-31   | 2026-07-30  | +85.66%               |      733,041,091 |     394,837,031 |        123.2  | +1.07%             |      5,950,009 |     3,239,024 |   357,006,520,913 |
| 0288.HK  |        |           | 2026-07-31   | 2026-07-30  | +73.86%               |      634,096,064 |     364,707,342 |          8.45 | -1.97%             |     75,040,956 |    42,309,437 |   108,415,352,750 |
| 0066.HK  |        |           | 2026-07-31   | 2026-07-30  | +69.64%               |      236,309,868 |     139,298,950 |         33.12 | -0.78%             |      7,134,960 |     4,173,126 |   205,813,638,671 |
| 0881.HK  |        |           | 2026-07-31   | 2026-07-30  | -60.90%               |       32,209,715 |      82,379,766 |          4.53 | -3.82%             |      7,110,312 |    17,490,396 |    10,722,482,696 |
| 1810.HK  |        |           | 2026-07-31   | 2026-07-30  | +58.51%               |   11,921,337,246 |   7,520,943,365 |         28.78 | -7.28%             |    414,222,966 |   242,298,426 |   739,461,381,480 |
| 1277.HK  |        |           | 2026-07-31   | 2026-07-30  | +54.87%               |       33,069,921 |      21,353,280 |          1.69 | -2.87%             |     19,568,000 |    12,272,000 |    14,533,169,012 |
| 2618.HK  |        |           | 2026-07-31   | 2026-07-30  | -54.48%               |      140,389,586 |     308,443,234 |         15.02 | -0.92%             |      9,346,843 |    20,345,860 |    92,008,781,562 |
| 2018.HK  |        |           | 2026-07-31   | 2026-07-30  | +53.84%               |      322,318,584 |     209,512,526 |         38.54 | +1.58%             |      8,363,222 |     5,522,207 |    44,544,956,998 |
| 1099.HK  |        |           | 2026-07-31   | 2026-07-30  | +52.79%               |      103,181,110 |      67,532,676 |         17.38 | -1.53%             |      5,936,773 |     3,826,214 |    54,237,001,980 |
| 1044.HK  |        |           | 2026-07-31   | 2026-07-30  | +51.21%               |      239,438,264 |     158,348,095 |         24.76 | -4.33%             |      9,670,366 |     6,118,551 |    28,489,250,368 |
| 1876.HK  |        |           | 2026-07-31   | 2026-07-30  | -49.32%               |      386,081,167 |     761,794,348 |          6.58 | -6.67%             |     58,674,950 |   108,055,933 |    87,051,879,036 |
| 0386.HK  |        |           | 2026-07-31   | 2026-07-30  | -46.42%               |      376,722,166 |     703,089,120 |          4.43 | -0.67%             |     85,038,867 |   157,643,299 |   534,965,344,712 |
| 0006.HK  |        |           | 2026-07-31   | 2026-07-30  | +46.39%               |      207,130,922 |     141,489,474 |         59.05 | -0.08%             |      3,507,721 |     2,394,069 |   125,841,757,717 |
| 0883.HK  |        |           | 2026-07-31   | 2026-07-30  | -45.84%               |    1,209,540,877 |   2,233,419,363 |         23.82 | -1.49%             |     50,778,375 |    92,366,391 | 1,132,163,489,393 |
| 2899.HK  |        |           | 2026-07-31   | 2026-07-30  | +45.73%               |    2,286,704,964 |   1,569,140,461 |         33.24 | +2.21%             |     68,793,768 |    48,251,551 |   883,875,398,666 |
| 1109.HK  |        |           | 2026-07-31   | 2026-07-30  | +43.29%               |      629,909,192 |     439,594,840 |         33.2  | -2.35%             |     18,973,168 |    12,929,260 |   236,747,199,463 |
| 1177.HK  |        |           | 2026-07-31   | 2026-07-30  | -42.88%               |      310,414,487 |     543,483,705 |          5.03 | -0.59%             |     61,712,619 |   107,407,848 |    89,403,109,734 |
| 1929.HK  |        |           | 2026-07-31   | 2026-07-30  | +41.09%               |      140,528,147 |      99,599,641 |         12.37 | +2.23%             |     11,360,400 |     8,231,375 |   122,046,515,814 |
| 0868.HK  |        |           | 2026-07-31   | 2026-07-30  | -40.90%               |       73,561,248 |     124,479,137 |          9.32 | +0.65%             |      7,892,838 |    13,442,671 |    41,263,602,873 |
| 2601.HK  |        |           | 2026-07-31   | 2026-07-30  | +40.71%               |      455,457,431 |     323,676,450 |         30.56 | -2.49%             |     14,903,712 |    10,327,902 |   293,997,629,726 |
| 9961.HK  |        |           | 2026-07-31   | 2026-07-30  | -40.42%               |    1,023,510,537 |   1,717,990,491 |        366.4  | -0.16%             |      2,793,424 |     4,681,173 |   230,723,989,497 |
| 0316.HK  |        |           | 2026-07-31   | 2026-07-30  | -38.21%               |       85,288,186 |     138,031,714 |        153.1  | -1.48%             |        557,075 |       888,235 |   101,103,155,801 |
| 6098.HK  |        |           | 2026-07-31   | 2026-07-30  | +35.35%               |       28,381,018 |      20,968,160 |          5.6  | -0.71%             |      5,068,039 |     3,717,759 |    18,169,936,028 |
| 1398.HK  |        |           | 2026-07-31   | 2026-07-30  | -35.03%               |    1,748,147,611 |   2,690,713,897 |          7.51 | -1.70%             |    232,775,973 |   352,187,689 | 2,676,611,072,313 |
| 9992.HK  |        |           | 2026-07-31   | 2026-07-30  | -34.67%               |    1,719,260,921 |   2,631,589,016 |        162.6  | -0.37%             |     10,573,560 |    16,124,933 |   213,246,567,712 |
| 0291.HK  |        |           | 2026-07-31   | 2026-07-30  | +33.79%               |      368,110,062 |     275,133,484 |         23.66 | -3.59%             |     15,558,329 |    11,211,633 |    76,753,039,505 |
| 1658.HK  |        |           | 2026-07-31   | 2026-07-30  | +33.08%               |      338,696,595 |     254,515,340 |          5.08 | -0.59%             |     66,672,559 |    49,807,306 |   610,082,862,576 |
| 2269.HK  |        |           | 2026-07-31   | 2026-07-30  | -32.54%               |      974,508,965 |   1,444,478,738 |         38.74 | +2.49%             |     25,155,109 |    38,213,724 |   159,076,078,314 |
| 1299.HK  |        |           | 2026-07-31   | 2026-07-30  | +31.76%               |    2,150,485,443 |   1,632,076,720 |         79.25 | -0.50%             |     27,135,463 |    20,490,605 |   816,684,374,275 |
| 2007.HK  |        |           | 2026-07-31   | 2026-07-30  | -31.11%               |       48,675,723 |      70,654,099 |          0.17 | +1.19%             |    286,327,781 |   420,560,118 |     7,906,602,443 |
| 9633.HK  |        |           | 2026-07-31   | 2026-07-30  | -30.51%               |      379,292,660 |     545,796,333 |         43.78 | -3.91%             |      8,663,606 |    11,979,726 |   492,370,285,263 |
| 0002.HK  |        |           | 2026-07-31   | 2026-07-30  | +29.84%               |      434,205,923 |     334,413,450 |         78.1  | -0.13%             |      5,559,615 |     4,276,387 |   197,315,785,661 |
| 2388.HK  |        |           | 2026-07-31   | 2026-07-30  | +29.04%               |      619,066,901 |     479,764,964 |         52.2  | -0.29%             |     11,859,519 |     9,164,565 |   551,899,137,951 |
| 0939.HK  |        |           | 2026-07-31   | 2026-07-30  | -28.86%               |    2,669,324,944 |   3,752,431,135 |          9.21 | -1.60%             |    289,828,983 |   400,900,777 | 2,409,339,523,216 |
| 0322.HK  |        |           | 2026-07-31   | 2026-07-30  | -28.61%               |      125,345,171 |     175,582,048 |         11.9  | -2.38%             |     10,533,208 |    14,403,778 |    67,074,542,533 |
| 2313.HK  |        |           | 2026-07-31   | 2026-07-30  | -28.33%               |      217,116,378 |     302,928,699 |         44.58 | +0.91%             |      4,870,264 |     6,856,693 |    66,996,431,498 |
| 1093.HK  |        |           | 2026-07-31   | 2026-07-30  | -28.07%               |      477,791,916 |     664,240,572 |          8.58 | +0.35%             |     55,686,704 |    77,688,954 |    97,858,774,990 |
| 0992.HK  |        |           | 2026-07-31   | 2026-07-30  | +27.92%               |    3,043,314,875 |   2,379,016,893 |         23.86 | +9.75%             |    127,548,818 |   109,430,401 |   295,975,178,516 |
| 2628.HK  |        |           | 2026-07-31   | 2026-07-30  | -26.22%               |    1,194,826,100 |   1,619,351,598 |         29.2  | +1.04%             |     40,918,701 |    56,032,928 |   825,329,407,564 |
| 2057.HK  |        |           | 2026-07-31   | 2026-07-30  | +26.19%               |      376,577,411 |     298,412,966 |        186.8  | -1.48%             |      2,015,939 |     1,573,908 |   142,064,520,012 |
| 3328.HK  |        |           | 2026-07-31   | 2026-07-30  | +25.75%               |      327,307,990 |     260,276,620 |          7.56 | -1.43%             |     43,294,708 |    33,934,370 |   668,030,203,669 |
| 2828.HK  |        |           | 2026-07-31   | 2026-07-30  | -24.46%               |    5,657,285,186 |   7,489,406,340 |         88.62 | -1.53%             |     63,837,565 |    83,215,626 |                   |
| 0960.HK  |        |           | 2026-07-31   | 2026-07-30  | -24.33%               |       78,628,951 |     103,910,251 |          6.86 | -0.87%             |     11,461,946 |    15,015,932 |    47,076,242,487 |
| 6690.HK  |        |           | 2026-07-31   | 2026-07-30  | -23.49%               |      442,093,049 |     577,833,880 |         22.6  | -0.53%             |     19,561,639 |    25,432,830 |   211,934,433,667 |
| 9888.HK  |        |           | 2026-07-31   | 2026-07-30  | +22.76%               |    1,536,106,950 |   1,251,333,395 |        105.9  | +3.72%             |     14,505,259 |    12,255,959 |   287,358,833,415 |
| 7747.HK  |        |           | 2026-07-31   | 2026-07-30  | +22.26%               |    3,125,919,487 |   2,556,761,297 |         77.46 | +49.25%            |     40,355,274 |    49,263,222 |                   |
| 2318.HK  |        |           | 2026-07-31   | 2026-07-30  | -22.24%               |    1,544,022,462 |   1,985,617,630 |         58.65 | -0.09%             |     26,326,043 |    33,826,535 | 1,062,013,230,636 |
| 1038.HK  |        |           | 2026-07-31   | 2026-07-30  | +22.08%               |      148,386,035 |     121,548,410 |         62.6  | +0.08%             |      2,370,384 |     1,943,220 |   157,727,641,312 |
| 6862.HK  |        |           | 2026-07-31   | 2026-07-30  | +22.03%               |      160,581,172 |     131,587,245 |         11.89 | -0.59%             |     13,505,565 |    11,002,278 |    64,390,039,321 |
| 0241.HK  |        |           | 2026-07-31   | 2026-07-30  | +21.84%               |      359,362,305 |     294,942,225 |          3.59 | +1.70%             |    100,100,923 |    83,553,039 |    58,069,329,076 |
| 1088.HK  |        |           | 2026-07-31   | 2026-07-30  | +21.63%               |      500,609,819 |     411,595,306 |         43.46 | -0.59%             |     11,518,864 |     9,414,348 |   942,622,794,994 |
| 9999.HK  |        |           | 2026-07-31   | 2026-07-30  | -21.53%               |    1,549,445,346 |   1,974,610,135 |        207.8  | +0.58%             |      7,456,426 |     9,557,648 |   665,219,963,621 |
| 1024.HK  |        |           | 2026-07-31   | 2026-07-30  | +21.33%               |    1,973,780,411 |   1,626,771,972 |         43.7  | +1.77%             |     45,166,599 |    37,884,770 |   189,075,922,272 |
| 0762.HK  |        |           | 2026-07-31   | 2026-07-30  | +20.98%               |      273,101,705 |     225,734,405 |          6.72 | -0.88%             |     40,640,136 |    33,294,159 |   205,618,553,580 |

[Download CSV report](reports/hk_volume_alerts_20260731.csv) · [Download XLSX report](reports/hk_volume_alerts_20260731.xlsx)

</details>
<!-- DAILY_ALERTS_END -->

## What it detects

A stock is included in the daily alert list when **all** of the following are true:

| Rule | Threshold |
|------|-----------|
| Turnover change | ≥ **+20%** or ≤ **−20%** vs prior session |
| Liquidity floor | Latest session turnover **> HKD 15,000,000** |
| Valid prior session | Prior session turnover > 0 (no divide-by-zero) |

Turnover is computed as `Close × Volume` (HKD). `Turnover_Pct_Change` and `Price_Pct_Change` are formatted with an explicit sign (e.g. `+83.91%`, `−30.26%`).

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
├── screener.py             # Trading value anomaly logic
├── readme_updater.py       # Collapsible daily alerts block for README.md
├── report_cleanup.py       # Deletes reports older than 30 days
├── reports/                # Daily CSV + XLSX archives (committed by CI)
├── .github/workflows/
│   └── daily_run.yml       # Scheduled GitHub Actions job
└── requirements.txt
```

## Output

Each successful run produces:

| Output | Location | Description |
|--------|----------|-------------|
| CSV report | `reports/hk_volume_alerts_YYYYMMDD.csv` | Full alert list |
| XLSX report | `reports/hk_volume_alerts_YYYYMMDD.xlsx` | Full alert list |
| Console table | stdout | Markdown-style table |
| GitHub summary | `github_summary.md` | Used by Actions for UI + email body |
| README toggle | `README.md` | Collapsible daily alert table on the repo homepage |

### Report columns

| Column | Description |
|--------|-------------|
| `Ticker` | Yahoo Finance symbol (e.g. `0700.HK`) |
| `Name` | English name |
| `Name_ZH` | Chinese name |
| `Date_Today` | Latest trading session in the dataset |
| `Date_Prev` | Prior trading session |
| `Turnover_Pct_Change` | Signed percent turnover change vs prior session |
| `Turnover_Today` | Trading turnover on latest session (Close × Volume, HKD) |
| `Turnover_Prev` | Trading turnover on prior session (Close × Volume, HKD) |
| `Close_Today` | Closing price on latest session (HKD) |
| `Price_Pct_Change` | Signed percent price change vs prior session |
| `Volume_Today` | Shares traded on latest session |
| `Volume_Prev` | Shares traded on prior session |
| `Market_Cap` | Total market capitalisation (HKD) |

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
4. Sends a **daily email** with the alert table and CSV + XLSX attachments (when configured)
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
| **yfinance / Yahoo Finance** | Daily OHLCV history, market cap (free, may be delayed) |
| **East Money** | Optional ticker enrichment (best-effort) |

## Design principles

- **Stateless** — no database; each run is independent
- **Holiday-aware dates** — derived from actual volume data, not hardcoded offsets
- **Graceful degradation** — missing tickers, empty batches, and API failures are logged and skipped without crashing the pipeline
- **Free infrastructure** — yfinance + GitHub Actions free tier

## Disclaimer

Market data is pulled from free, public sources and may be subject to exchange delays, omissions, or inaccuracies. This tool is for informational purposes only and is not investment advice.
