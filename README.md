# HK Abnormal Stock Track

A stateless, end-of-day (EOD) trading-value screener for the Hong Kong Stock Exchange (HKEX). Each run discovers active HK listings, pulls recent daily data via [yfinance](https://github.com/ranaroussi/yfinance), and flags stocks whose turnover (Close × Volume) shifted significantly versus the **prior trading session**.

No database is required — all data is fetched and processed in memory.

## Latest alerts

<!-- DAILY_ALERTS_START -->
<details>
<summary><strong>📊 Daily trading value alerts — 69 stocks (2026-08-19 vs 2026-08-18) · click to expand</strong></summary>

> **Latest session:** 2026-08-19 · **Prior session:** 2026-08-18 · **Updated:** 2026-08-19 09:47:46 HKT  
> Filters: turnover change ≥ +20% or ≤ −20% · minimum turnover &gt; HKD 15,000,000

| Ticker   | Name           | Name_ZH   | Date_Today   | Date_Prev   | Turnover_Pct_Change   |   Turnover_Today |   Turnover_Prev |   Close_Today | Price_Pct_Change   |   Volume_Today |   Volume_Prev |        Market_Cap |
|----------|----------------|-----------|--------------|-------------|-----------------------|------------------|-----------------|---------------|--------------------|----------------|---------------|-------------------|
| 0003.HK  | HK & CHINA GAS | 香港中华煤气    | 2026-08-19   | 2026-08-18  | +1340.48%             |    1,622,943,349 |     112,666,768 |         7.285 | +7.37%             |    222,778,776 |    16,605,272 |   135,937,150,816 |
| 0762.HK  |                |           | 2026-08-19   | 2026-08-18  | +881.07%              |    1,741,010,937 |     177,461,314 |         5.495 | -12.36%            |    316,835,482 |    28,303,240 |   168,136,006,498 |
| 9888.HK  |                |           | 2026-08-19   | 2026-08-18  | +380.69%              |    3,424,543,722 |     712,426,313 |        89.95  | -11.03%            |     38,071,638 |     7,046,749 |   244,078,619,606 |
| 0291.HK  |                |           | 2026-08-19   | 2026-08-18  | +161.18%              |      426,436,979 |     163,273,128 |        21.06  | -4.96%             |     20,248,670 |     7,367,921 |    68,318,638,267 |
| 2057.HK  |                |           | 2026-08-19   | 2026-08-18  | +156.43%              |      582,103,984 |     227,000,130 |       176     | -3.72%             |      3,307,409 |     1,241,795 |   133,761,267,728 |
| 0200.HK  |                |           | 2026-08-19   | 2026-08-18  | +140.41%              |       22,949,150 |       9,545,720 |         3.23  | -3.29%             |      7,105,000 |     2,858,000 |     7,347,967,822 |
| 1801.HK  |                |           | 2026-08-19   | 2026-08-18  | +133.56%              |    1,814,105,882 |     776,727,157 |        98.25  | +1.66%             |     18,464,182 |     8,036,494 |   171,045,470,368 |
| 1088.HK  |                |           | 2026-08-19   | 2026-08-18  | +122.94%              |      495,450,766 |     222,232,377 |        44.28  | +1.47%             |     11,189,042 |     5,092,401 |   960,408,124,504 |
| 6098.HK  |                |           | 2026-08-19   | 2026-08-18  | +106.13%              |       29,178,913 |      14,155,708 |         5.375 | +0.75%             |      5,428,635 |     2,653,366 |    17,439,894,253 |
| 1810.HK  |                |           | 2026-08-19   | 2026-08-18  | +98.77%               |    9,326,197,923 |   4,691,901,403 |        27.44  | +4.81%             |    339,876,011 |   179,217,011 |   706,255,282,392 |
| 0012.HK  | HENDERSON LAND | 恒基地产      | 2026-08-19   | 2026-08-18  | +95.90%               |      252,766,878 |     129,030,229 |        27.8   | +2.28%             |      9,092,334 |     4,747,249 |   134,590,554,989 |
| 0836.HK  |                |           | 2026-08-19   | 2026-08-18  | +91.20%               |      278,522,969 |     145,674,291 |        17.88  | -1.27%             |     15,577,348 |     8,043,859 |    92,565,788,046 |
| 1277.HK  |                |           | 2026-08-19   | 2026-08-18  | +80.55%               |       29,818,051 |      16,514,800 |         2.055 | +0.24%             |     14,510,000 |     8,056,000 |    17,671,989,514 |
| 0016.HK  | SHK PPT        | 新鸿基地产     | 2026-08-19   | 2026-08-18  | +77.46%               |      513,492,223 |     289,352,246 |       120.2   | +2.47%             |      4,271,982 |     2,466,771 |   348,313,180,091 |
| 3988.HK  |                |           | 2026-08-19   | 2026-08-18  | +71.90%               |    1,235,727,047 |     718,872,306 |         5.41  | +1.69%             |    228,415,357 |   135,126,369 | 1,743,169,098,748 |
| 0023.HK  | BANK OF E ASIA | 东亚银行      | 2026-08-19   | 2026-08-18  | +70.80%               |       34,358,779 |      20,115,847 |        16.28  | -0.43%             |      2,110,490 |     1,230,327 |    43,041,455,867 |
| 0388.HK  |                |           | 2026-08-19   | 2026-08-18  | +65.53%               |    1,990,870,672 |   1,202,696,910 |       414.6   | +2.37%             |      4,801,907 |     2,969,622 |   524,067,290,166 |
| 0975.HK  |                |           | 2026-08-19   | 2026-08-18  | +64.65%               |       93,419,819 |      56,737,447 |         9.62  | -1.23%             |      9,711,000 |     5,825,200 |     9,841,608,954 |
| 0101.HK  |                |           | 2026-08-19   | 2026-08-18  | -59.11%               |       22,833,705 |      55,843,174 |         7.16  | +0.14%             |      3,189,065 |     7,810,234 |    37,254,070,106 |
| 1209.HK  |                |           | 2026-08-19   | 2026-08-18  | -56.09%               |      147,199,000 |     335,263,232 |        40.84  | +2.05%             |      3,604,285 |     8,377,392 |    93,217,300,348 |
| 0014.HK  | HYSAN DEV      | 希慎兴业      | 2026-08-19   | 2026-08-18  | +55.08%               |       52,331,688 |      33,745,632 |        16.86  | -0.24%             |      3,103,896 |     1,996,783 |    17,315,359,266 |
| 9992.HK  |                |           | 2026-08-19   | 2026-08-18  | -53.85%               |    1,084,494,572 |   2,349,866,630 |       150.5   | +0.27%             |      7,205,944 |    15,655,340 |   197,377,658,278 |
| 0688.HK  |                |           | 2026-08-19   | 2026-08-18  | +53.11%               |      436,365,744 |     284,999,430 |        13.96  | +0.50%             |     31,258,291 |    20,518,317 |   152,790,574,566 |
| 2382.HK  |                |           | 2026-08-19   | 2026-08-18  | -52.37%               |      576,651,017 |   1,210,814,006 |        58.4   | -3.31%             |      9,874,161 |    20,046,589 |    62,731,809,959 |
| 2015.HK  |                |           | 2026-08-19   | 2026-08-18  | +51.92%               |      328,248,699 |     216,061,569 |        47.9   | +0.04%             |      6,852,791 |     4,512,564 |    93,912,357,684 |
| 0020.HK  | SENSETIME-W    | 商汤－Ｗ      | 2026-08-19   | 2026-08-18  | -51.49%               |      587,597,905 |   1,211,238,469 |         1.43  | -2.39%             |    410,907,641 |   826,783,919 |    57,938,722,580 |
| 1398.HK  |                |           | 2026-08-19   | 2026-08-18  | +51.27%               |    1,177,580,691 |     778,455,180 |         7.385 | +1.51%             |    159,455,742 |   107,004,147 | 2,632,060,290,177 |
| 6862.HK  |                |           | 2026-08-19   | 2026-08-18  | -50.87%               |      112,381,929 |     228,742,067 |        11.48  | -0.26%             |      9,789,367 |    19,873,333 |    62,169,688,864 |
| 6690.HK  |                |           | 2026-08-19   | 2026-08-18  | +49.53%               |      386,859,260 |     258,717,353 |        21.24  | +2.02%             |     18,213,713 |    12,426,386 |   199,180,851,619 |
| 0005.HK  | HSBC HOLDINGS  | 汇丰控股      | 2026-08-19   | 2026-08-18  | +47.44%               |    1,361,375,725 |     923,351,623 |       161.2   | -0.56%             |      8,445,259 |     5,696,185 | 2,762,817,949,644 |
| 2269.HK  |                |           | 2026-08-19   | 2026-08-18  | -45.42%               |    1,532,089,165 |   2,807,003,855 |        47.9   | -1.40%             |     31,985,159 |    57,781,057 |   196,689,315,019 |
| 6186.HK  |                |           | 2026-08-19   | 2026-08-18  | -44.64%               |       20,575,257 |      37,167,102 |         3.215 | +0.31%             |      6,399,769 |    11,596,600 |    28,316,641,267 |
| 9633.HK  |                |           | 2026-08-19   | 2026-08-18  | -44.54%               |       99,186,265 |     178,848,664 |        42.14  | -0.05%             |      2,353,732 |     4,242,141 |   473,926,087,231 |
| 1997.HK  |                |           | 2026-08-19   | 2026-08-18  | +43.26%               |      125,322,253 |      87,478,528 |        32.28  | +0.87%             |      3,882,350 |     2,733,704 |    98,009,414,409 |
| 3931.HK  |                |           | 2026-08-19   | 2026-08-18  | -42.63%               |       65,986,240 |     115,011,386 |        20     | -3.94%             |      3,299,312 |     5,524,082 |    35,446,037,160 |
| 1288.HK  |                |           | 2026-08-19   | 2026-08-18  | +42.47%               |      751,050,053 |     527,160,462 |         6.22  | +2.13%             |    120,747,601 |    86,561,650 | 2,176,894,397,260 |
| 9988.HK  |                |           | 2026-08-19   | 2026-08-18  | -42.43%               |    8,784,394,531 |  15,258,962,853 |       124.2   | -1.97%             |     70,727,816 |   120,433,806 | 2,381,533,565,098 |
| 0883.HK  |                |           | 2026-08-19   | 2026-08-18  | -42.27%               |    1,055,140,080 |   1,827,564,772 |        24.46  | +0.16%             |     43,137,372 |    74,838,852 | 1,162,582,630,933 |
| 1044.HK  |                |           | 2026-08-19   | 2026-08-18  | +39.02%               |      121,283,179 |      87,239,320 |        24.12  | +1.26%             |      5,028,324 |     3,662,440 |    27,752,856,883 |
| 2318.HK  |                |           | 2026-08-19   | 2026-08-18  | -37.54%               |    1,879,444,497 |   3,009,227,707 |        54.3   | +0.74%             |     34,612,238 |    55,829,826 |   983,244,946,513 |
| 0175.HK  |                |           | 2026-08-19   | 2026-08-18  | -35.62%               |    1,043,400,974 |   1,620,573,979 |        17.93  | -1.81%             |     58,193,026 |    88,749,943 |   193,377,359,035 |
| 1093.HK  |                |           | 2026-08-19   | 2026-08-18  | +34.68%               |      585,002,556 |     434,379,141 |         8.685 | -1.31%             |     67,357,804 |    49,361,265 |    99,056,353,078 |
| 2899.HK  |                |           | 2026-08-19   | 2026-08-18  | +33.76%               |    1,391,742,715 |   1,040,485,582 |        34.9   | -1.69%             |     39,878,013 |    29,309,453 |   928,015,980,882 |
| 1361.HK  |                |           | 2026-08-19   | 2026-08-18  | -33.55%               |       35,993,929 |      54,166,763 |         4.93  | +2.60%             |      7,301,000 |    11,273,000 |    10,686,671,887 |
| 1658.HK  |                |           | 2026-08-19   | 2026-08-18  | +33.31%               |      231,377,095 |     173,565,541 |         4.905 | +1.76%             |     47,171,679 |    36,009,447 |   589,066,262,575 |
| 0384.HK  |                |           | 2026-08-19   | 2026-08-18  | +33.04%               |       76,240,181 |      57,305,179 |         5.76  | +2.13%             |     13,236,142 |    10,160,493 |    31,381,361,035 |
| 0241.HK  |                |           | 2026-08-19   | 2026-08-18  | -32.99%               |      174,689,183 |     260,701,722 |         3.255 | +0.00%             |     53,667,950 |    80,092,692 |    52,650,606,492 |
| 2601.HK  |                |           | 2026-08-19   | 2026-08-18  | -31.09%               |      188,712,448 |     273,841,522 |        28.46  | +0.92%             |      6,630,796 |     9,710,692 |   273,794,909,001 |
| 0316.HK  |                |           | 2026-08-19   | 2026-08-18  | +30.74%               |      373,815,430 |     285,929,993 |       166.9   | +1.21%             |      2,239,757 |     1,733,960 |   110,216,299,238 |
| 2628.HK  |                |           | 2026-08-19   | 2026-08-18  | -30.65%               |    1,335,893,863 |   1,926,277,000 |        26.96  | +0.30%             |     49,550,961 |    71,662,093 |   762,016,420,922 |
| 2618.HK  |                |           | 2026-08-19   | 2026-08-18  | -29.61%               |      225,196,389 |     319,944,041 |        11.51  | -1.29%             |     19,565,281 |    27,439,455 |    70,423,130,884 |
| 3690.HK  |                |           | 2026-08-19   | 2026-08-18  | -29.33%               |    3,199,859,397 |   4,528,017,253 |        87.05  | +1.75%             |     36,758,866 |    52,928,312 |   537,258,791,987 |
| 1109.HK  |                |           | 2026-08-19   | 2026-08-18  | +28.43%               |      347,519,004 |     270,588,461 |        34.16  | -0.23%             |     10,173,273 |     7,902,700 |   243,592,894,930 |
| 3328.HK  |                |           | 2026-08-19   | 2026-08-18  | +28.38%               |      178,745,594 |     139,233,241 |         7.425 | +1.09%             |     24,073,480 |    18,956,194 |   656,101,114,709 |
| 0823.HK  |                |           | 2026-08-19   | 2026-08-18  | +28.35%               |      237,110,040 |     184,735,789 |        38.74  | +0.26%             |      6,120,548 |     4,780,947 |   101,100,170,012 |
| 0267.HK  |                |           | 2026-08-19   | 2026-08-18  | -27.26%               |      161,494,878 |     222,010,290 |        12.36  | +1.31%             |     13,065,929 |    18,197,565 |   359,555,636,119 |
| 1876.HK  |                |           | 2026-08-19   | 2026-08-18  | +26.64%               |       45,713,531 |      36,097,813 |         6.335 | -1.09%             |      7,216,027 |     5,635,880 |    83,810,587,145 |
| 1928.HK  |                |           | 2026-08-19   | 2026-08-18  | -25.34%               |      131,128,257 |     175,631,231 |        14.45  | +0.56%             |      9,074,620 |    12,222,076 |   116,949,333,185 |
| 9999.HK  |                |           | 2026-08-19   | 2026-08-18  | +25.08%               |    1,178,722,396 |     942,384,298 |       194.4   | +0.31%             |      6,063,387 |     4,862,664 |   622,323,171,167 |
| 1211.HK  |                |           | 2026-08-19   | 2026-08-18  | -24.86%               |      836,065,328 |   1,112,678,010 |        89.4   | -0.67%             |      9,351,961 |    12,363,089 |   815,077,476,222 |
| 0322.HK  |                |           | 2026-08-19   | 2026-08-18  | -24.19%               |      398,486,101 |     525,640,405 |        13.88  | +2.21%             |     28,709,373 |    38,706,952 |    78,234,847,721 |
| 2020.HK  |                |           | 2026-08-19   | 2026-08-18  | +23.66%               |      448,303,140 |     362,543,018 |        73.65  | +2.15%             |      6,086,940 |     5,028,336 |   204,047,298,809 |
| 2018.HK  |                |           | 2026-08-19   | 2026-08-18  | -23.52%               |      153,134,619 |     200,236,546 |        41.66  | -3.21%             |      3,675,819 |     4,652,336 |    48,151,086,083 |
| 9961.HK  |                |           | 2026-08-19   | 2026-08-18  | -22.42%               |      542,385,526 |     699,089,226 |       352.4   | +0.63%             |      1,539,119 |     1,996,257 |   221,908,116,389 |
| 1099.HK  |                |           | 2026-08-19   | 2026-08-18  | -21.64%               |       74,348,683 |      94,884,732 |        16.74  | -1.01%             |      4,441,379 |     5,611,161 |    52,239,783,923 |
| 6618.HK  |                |           | 2026-08-19   | 2026-08-18  | -21.57%               |      321,520,883 |     409,968,444 |        38.9   | +1.04%             |      8,265,318 |    10,648,531 |   124,072,761,194 |
| 2688.HK  |                |           | 2026-08-19   | 2026-08-18  | +21.16%               |      181,748,559 |     150,002,829 |        47.2   | +0.38%             |      3,850,605 |     3,190,192 |    52,479,540,989 |
| 0669.HK  |                |           | 2026-08-19   | 2026-08-18  | -20.77%               |      930,648,257 |   1,174,684,152 |       138.5   | -1.98%             |      6,719,482 |     8,313,405 |   253,127,854,828 |
| 0981.HK  |                |           | 2026-08-19   | 2026-08-18  | +20.36%               |   10,193,218,198 |   8,468,849,615 |        73     | -3.76%             |    139,633,126 |   111,652,601 |   624,938,837,635 |

[Download CSV report](reports/hk_volume_alerts_20260819.csv) · [Download XLSX report](reports/hk_volume_alerts_20260819.xlsx)

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
