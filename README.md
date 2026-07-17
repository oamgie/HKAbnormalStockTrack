# HK Abnormal Stock Track

A stateless, end-of-day (EOD) trading-value screener for the Hong Kong Stock Exchange (HKEX). Each run discovers active HK listings, pulls recent daily data via [yfinance](https://github.com/ranaroussi/yfinance), and flags stocks whose turnover (Close × Volume) shifted significantly versus the **prior trading session**.

No database is required — all data is fetched and processed in memory.

## Latest alerts

<!-- DAILY_ALERTS_START -->
<details>
<summary><strong>📊 Daily trading value alerts — 93 stocks (2026-07-17 vs 2026-07-16) · click to expand</strong></summary>

> **Latest session:** 2026-07-17 · **Prior session:** 2026-07-16 · **Updated:** 2026-07-17 10:57:58 HKT  
> Filters: turnover change ≥ +20% or ≤ −20% · minimum turnover &gt; HKD 15,000,000

| Ticker   | Name            | Name_ZH       | Date_Today   | Date_Prev   | Turnover_Pct_Change   |   Turnover_Today |   Turnover_Prev |   Close_Today | Price_Pct_Change   |   Volume_Today |   Volume_Prev |        Market_Cap |
|----------|-----------------|---------------|--------------|-------------|-----------------------|------------------|-----------------|---------------|--------------------|----------------|---------------|-------------------|
| 0209.HK  | POLY XVERSE IT  | 万维智能科技        | 2026-07-17   | 2026-07-16  | +1677.06%             |      169,456,942 |       9,535,800 |         0.48  | +4.35%             |    353,035,304 |    20,730,000 |       713,122,451 |
| 2291.HK  |                 |               | 2026-07-17   | 2026-07-16  | +812.12%              |      111,264,567 |      12,198,485 |        11.07  | -1.34%             |     10,051,000 |     1,087,209 |     3,817,921,091 |
| 6162.HK  |                 | 天瑞汽车内饰        | 2026-07-17   | 2026-07-16  | +447.15%              |       39,644,001 |       7,245,520 |         0.55  | +34.15%            |     72,080,000 |    17,672,000 |     1,320,000,028 |
| 3110.HK  |                 |               | 2026-07-17   | 2026-07-16  | +360.71%              |       63,616,802 |      13,808,415 |        30.4   | -0.26%             |      2,092,658 |       453,032 |                   |
| 0117.HK  | TIANLI HOLDINGS | 天利控股集团        | 2026-07-17   | 2026-07-16  | +292.67%              |       27,381,548 |       6,973,180 |         2.64  | -12.58%            |     10,371,798 |     2,309,000 |     1,966,140,078 |
| 1836.HK  |                 | 九兴控股          | 2026-07-17   | 2026-07-16  | +237.80%              |       57,785,861 |      17,106,625 |        13.64  | +6.65%             |      4,236,500 |     1,337,500 |    11,473,879,628 |
| 0006.HK  | POWER ASSETS    | 电能实业          | 2026-07-17   | 2026-07-16  | +210.95%              |      297,828,873 |      95,779,538 |        59.8   | +3.01%             |      4,980,416 |     1,649,949 |   127,440,086,583 |
| 0285.HK  |                 |               | 2026-07-17   | 2026-07-16  | +198.35%              |      839,886,655 |     281,505,913 |        23.98  | +2.22%             |     35,024,465 |    11,999,400 |    53,861,680,801 |
| 0003.HK  | HK & CHINA GAS  | 香港中华煤气        | 2026-07-17   | 2026-07-16  | +197.97%              |      254,127,683 |      85,285,773 |         6.8   | +1.64%             |     37,371,717 |    12,748,247 |   126,887,120,225 |
| 1038.HK  |                 |               | 2026-07-17   | 2026-07-16  | +187.10%              |      136,812,428 |      47,653,174 |        62.25  | +1.63%             |      2,197,790 |       778,011 |   156,845,781,326 |
| 1109.HK  |                 |               | 2026-07-17   | 2026-07-16  | +179.19%              |    1,814,276,982 |     649,824,373 |        33.72  | -2.60%             |     53,804,179 |    18,770,202 |   240,455,291,308 |
| 0179.HK  | JOHNSON ELEC H  | 德昌电机控股        | 2026-07-17   | 2026-07-16  | +175.74%              |      241,168,984 |      87,463,217 |        17.53  | -10.65%            |     13,757,500 |     4,457,860 |    16,245,455,422 |
| 6110.HK  |                 | 滔搏            | 2026-07-17   | 2026-07-16  | +173.52%              |       52,767,569 |      19,292,172 |         1.91  | +3.24%             |     27,627,000 |    10,428,201 |    11,844,333,858 |
| 1798.HK  |                 | 大唐新能源         | 2026-07-17   | 2026-07-16  | +172.37%              |       42,223,941 |      15,502,426 |         1.28  | +3.23%             |     32,987,455 |    12,501,956 |     9,310,337,071 |
| 0291.HK  |                 |               | 2026-07-17   | 2026-07-16  | +163.26%              |      529,101,166 |     200,983,859 |        23.7   | -0.17%             |     22,324,943 |     8,466,043 |    76,882,802,474 |
| 0133.HK  | CHINA MERCHANTS | 招商局中国基金       | 2026-07-17   | 2026-07-16  | +163.09%              |       62,434,290 |      23,731,524 |        25.44  | +5.47%             |      2,454,178 |       983,894 |     3,875,351,932 |
| 0857.HK  |                 |               | 2026-07-17   | 2026-07-16  | +162.70%              |    1,168,086,607 |     444,648,550 |         9.59  | +1.27%             |    121,802,564 |    46,953,383 | 1,755,171,205,201 |
| 7568.HK  |                 | 南方两倍做空纳斯达克100 | 2026-07-17   | 2026-07-16  | +151.82%              |       30,993,504 |      12,307,569 |         2.492 | +5.95%             |     12,437,200 |     5,232,810 |                   |
| 0902.HK  |                 | 华能国际电力股份      | 2026-07-17   | 2026-07-16  | +133.01%              |      262,363,426 |     112,598,531 |         5.79  | +3.21%             |     45,313,200 |    20,071,039 |    90,891,959,949 |
| 0981.HK  |                 |               | 2026-07-17   | 2026-07-16  | +117.85%              |   16,721,335,305 |   7,675,487,194 |        67.7   | -9.97%             |    246,991,670 |   102,067,653 |   579,566,539,735 |
| 0568.HK  |                 | 山东墨龙          | 2026-07-17   | 2026-07-16  | +101.62%              |      740,083,504 |     367,074,513 |         5.8   | +5.84%             |    127,600,600 |    66,984,400 |     5,387,211,480 |
| 0177.HK  | JIANGSU EXPRESS | 江苏宁沪高速公路      | 2026-07-17   | 2026-07-16  | +90.57%               |       48,867,722 |      25,642,575 |         9.87  | +0.20%             |      4,951,137 |     2,603,307 |    49,722,567,248 |
| 1658.HK  |                 |               | 2026-07-17   | 2026-07-16  | +80.42%               |      213,770,681 |     118,487,280 |         4.85  | +1.04%             |     44,076,430 |    24,684,849 |   582,460,997,983 |
| 0119.HK  | POLY PROPERTY   | 保利置业集团        | 2026-07-17   | 2026-07-16  | +79.08%               |       27,428,484 |      15,316,079 |         1.5   | -3.85%             |     18,285,656 |     9,818,000 |     5,731,774,677 |
| 7347.HK  |                 | 南方两倍做空三星电子    | 2026-07-17   | 2026-07-16  | +78.09%               |      117,963,499 |      66,238,512 |         1.672 | +24.04%            |     70,552,330 |    49,138,360 |                   |
| 7747.HK  |                 |               | 2026-07-17   | 2026-07-16  | +75.91%               |    3,472,284,994 |   1,973,886,080 |        67.2   | -19.04%            |     51,670,910 |    23,781,760 |                   |
| 0004.HK  | WHARF HOLDINGS  | 九龙仓集团         | 2026-07-17   | 2026-07-16  | +72.88%               |       22,581,724 |      13,062,144 |        18.81  | -1.57%             |      1,200,517 |       683,524 |    57,483,872,388 |
| 0836.HK  |                 |               | 2026-07-17   | 2026-07-16  | +70.39%               |      388,657,683 |     228,095,641 |        18.17  | +1.79%             |     21,390,076 |    12,778,467 |    94,067,139,530 |
| 1876.HK  |                 |               | 2026-07-17   | 2026-07-16  | +69.37%               |       90,305,634 |      53,317,431 |         6.54  | +0.77%             |     13,808,201 |     8,215,321 |    86,522,688,781 |
| 0068.HK  | MANYCORE TECH   | MANYCORE TECH | 2026-07-17   | 2026-07-16  | +69.22%               |       30,450,369 |      17,995,072 |         8.08  | -17.64%            |      3,768,610 |     1,834,360 |    13,753,023,137 |
| 2359.HK  |                 |               | 2026-07-17   | 2026-07-16  | +68.45%               |    1,800,306,783 |   1,068,753,528 |       153     | -5.56%             |     11,766,711 |     6,597,244 |   456,514,844,715 |
| 3968.HK  |                 |               | 2026-07-17   | 2026-07-16  | +65.57%               |      535,496,180 |     323,424,755 |        47.08  | +1.68%             |     11,374,175 |     6,985,416 | 1,187,350,377,073 |
| 1209.HK  |                 |               | 2026-07-17   | 2026-07-16  | -64.74%               |      139,458,769 |     395,540,966 |        39.42  | -1.40%             |      3,537,767 |     9,893,471 |    89,976,145,820 |
| 0083.HK  | SINO LAND       | 信和置业          | 2026-07-17   | 2026-07-16  | -64.65%               |       37,595,397 |     106,343,444 |        10.56  | -0.38%             |      3,560,170 |    10,032,400 |   101,229,655,590 |
| 0918.HK  |                 | 龙翼航空科技        | 2026-07-17   | 2026-07-16  | -62.90%               |       18,648,096 |      50,258,148 |         1.88  | +12.57%            |      9,919,200 |    30,094,700 |     2,094,450,013 |
| 0066.HK  | MTR CORPORATION | 港铁公司          | 2026-07-17   | 2026-07-16  | +62.40%               |      286,907,704 |     176,666,507 |        32.52  | +2.07%             |      8,822,500 |     5,545,088 |   202,085,140,086 |
| 6098.HK  |                 |               | 2026-07-17   | 2026-07-16  | +60.11%               |       96,145,699 |      60,050,663 |         5.66  | -1.05%             |     16,986,873 |    10,498,368 |    18,366,877,732 |
| 1070.HK  |                 | TCL电子         | 2026-07-17   | 2026-07-16  | -57.53%               |      282,272,920 |     664,711,974 |        14.25  | +5.71%             |     19,808,626 |    49,310,979 |    35,921,655,089 |
| 0316.HK  |                 | 东方海外国际        | 2026-07-17   | 2026-07-16  | +56.77%               |      223,508,510 |     142,573,604 |       145     | +2.91%             |      1,541,438 |     1,011,878 |    95,754,128,065 |
| 9992.HK  |                 |               | 2026-07-17   | 2026-07-16  | -56.66%               |    1,971,853,368 |   4,549,806,028 |       163.6   | -2.68%             |     12,052,893 |    27,066,067 |   216,073,628,955 |
| 1288.HK  |                 |               | 2026-07-17   | 2026-07-16  | +56.55%               |      512,136,901 |     327,144,796 |         5.68  | +1.25%             |     90,164,950 |    58,314,579 | 1,987,903,572,320 |
| 2269.HK  |                 |               | 2026-07-17   | 2026-07-16  | +54.31%               |    1,899,352,943 |   1,230,850,308 |        36.98  | -5.95%             |     51,361,627 |    31,303,416 |   151,849,071,976 |
| 2313.HK  |                 |               | 2026-07-17   | 2026-07-16  | -53.39%               |      281,480,869 |     603,937,170 |        44.4   | -1.33%             |      6,339,659 |    13,420,826 |    66,725,920,559 |
| 6618.HK  |                 |               | 2026-07-17   | 2026-07-16  | -50.60%               |      281,395,641 |     569,630,499 |        37.22  | -5.05%             |      7,560,334 |    14,531,390 |   118,714,348,122 |
| 2318.HK  |                 |               | 2026-07-17   | 2026-07-16  | +50.47%               |    1,728,383,809 |   1,148,622,890 |        54.6   | -0.36%             |     31,655,382 |    20,960,272 |   988,677,225,296 |
| 2057.HK  |                 |               | 2026-07-17   | 2026-07-16  | -49.85%               |      236,258,199 |     471,090,474 |       189.2   | -2.17%             |      1,248,722 |     2,435,835 |   143,889,755,427 |
| 0968.HK  |                 |               | 2026-07-17   | 2026-07-16  | +48.96%               |      145,764,647 |      97,851,872 |         2.01  | -1.47%             |     72,519,725 |    47,966,605 |    18,385,557,578 |
| 0960.HK  |                 |               | 2026-07-17   | 2026-07-16  | +47.79%               |      151,032,514 |     102,192,888 |         6.67  | -1.77%             |     22,643,555 |    15,050,499 |    45,772,381,176 |
| 2007.HK  |                 |               | 2026-07-17   | 2026-07-16  | -47.05%               |       48,787,980 |      92,139,309 |         0.179 | -6.28%             |    272,558,540 |   482,404,761 |     8,299,482,889 |
| 6862.HK  |                 |               | 2026-07-17   | 2026-07-16  | -46.82%               |      163,396,102 |     307,223,325 |        11.66  | -1.77%             |     14,013,388 |    25,882,336 |    63,144,476,618 |
| 0123.HK  | YUEXIU PROPERTY | 越秀地产          | 2026-07-17   | 2026-07-16  | -46.31%               |       15,168,936 |      28,250,260 |         3.66  | -2.66%             |      4,144,518 |     7,513,367 |    14,732,938,407 |
| 2687.HK  |                 | 卓越睿新          | 2026-07-17   | 2026-07-16  | +46.13%               |       45,178,841 |      30,916,640 |       203.6   | +4.84%             |        221,900 |       159,200 |    13,573,340,526 |
| 2618.HK  |                 |               | 2026-07-17   | 2026-07-16  | +45.98%               |      147,590,007 |     101,106,175 |        13.39  | -1.90%             |     11,022,405 |     7,407,046 |    82,023,806,868 |
| 1024.HK  |                 |               | 2026-07-17   | 2026-07-16  | -45.37%               |    3,620,364,887 |   6,627,140,398 |        43.28  | -7.76%             |     83,649,838 |   141,243,407 |   187,303,413,140 |
| 0288.HK  |                 |               | 2026-07-17   | 2026-07-16  | +43.73%               |      269,898,910 |     187,781,752 |         8.24  | -0.72%             |     32,754,723 |    22,624,307 |   105,721,006,155 |
| 2688.HK  |                 |               | 2026-07-17   | 2026-07-16  | -43.43%               |       85,941,700 |     151,910,988 |        42.02  | -1.27%             |      2,045,257 |     3,569,337 |    46,720,133,490 |
| 1177.HK  |                 |               | 2026-07-17   | 2026-07-16  | +42.73%               |      757,111,574 |     530,459,988 |         4.98  | -5.32%             |    152,030,436 |   100,847,902 |    88,514,407,477 |
| 0002.HK  | CLP HOLDINGS    | 中电控股          | 2026-07-17   | 2026-07-16  | +38.54%               |      322,557,241 |     232,823,142 |        77.7   | +1.11%             |      4,151,316 |     3,029,579 |   196,305,201,578 |
| 0388.HK  |                 |               | 2026-07-17   | 2026-07-16  | +38.26%               |    2,303,386,474 |   1,665,942,208 |       391     | -1.31%             |      5,891,014 |     4,204,801 |   494,236,149,152 |
| 9633.HK  |                 |               | 2026-07-17   | 2026-07-16  | +36.95%               |      356,793,124 |     260,528,583 |        42.22  | +0.48%             |      8,450,808 |     6,200,109 |   474,825,825,136 |
| 0881.HK  |                 |               | 2026-07-17   | 2026-07-16  | -35.90%               |       41,619,471 |      64,933,543 |         4.31  | -6.91%             |      9,656,490 |    14,024,523 |    10,201,743,414 |
| 0322.HK  |                 |               | 2026-07-17   | 2026-07-16  | -35.54%               |      143,875,422 |     223,193,969 |        11.59  | +1.31%             |     12,413,755 |    19,509,963 |    65,327,225,472 |
| 0012.HK  | HENDERSON LAND  | 恒基地产          | 2026-07-17   | 2026-07-16  | -34.21%               |      217,276,241 |     330,232,261 |        27.26  | -0.29%             |      7,970,515 |    12,078,722 |   131,976,210,809 |
| 0384.HK  |                 |               | 2026-07-17   | 2026-07-16  | -34.13%               |       49,414,236 |      75,018,174 |         5.69  | -1.22%             |      8,684,400 |    13,023,988 |    30,999,989,408 |
| 2015.HK  |                 |               | 2026-07-17   | 2026-07-16  | +33.26%               |      664,156,451 |     498,381,675 |        48.94  | -2.90%             |     13,570,831 |     9,888,525 |    97,243,485,099 |
| 0165.HK  | CHINA EB LTD    | 中国光大控股        | 2026-07-17   | 2026-07-16  | +32.30%               |       53,119,358 |      40,151,321 |         5.68  | -5.49%             |      9,352,000 |     6,680,752 |     9,572,240,794 |
| 0823.HK  |                 |               | 2026-07-17   | 2026-07-16  | +31.94%               |      465,834,662 |     353,078,704 |        39.22  | +1.13%             |     11,877,477 |     9,104,660 |   101,843,582,103 |
| 1928.HK  |                 |               | 2026-07-17   | 2026-07-16  | -31.71%               |      182,931,058 |     267,867,565 |        13.08  | -1.73%             |     13,985,555 |    20,125,286 |   105,861,404,105 |
| 0688.HK  |                 |               | 2026-07-17   | 2026-07-16  | -31.43%               |      272,537,086 |     397,440,399 |        13.37  | -1.40%             |     20,384,225 |    29,309,763 |   146,333,091,610 |
| 2899.HK  |                 |               | 2026-07-17   | 2026-07-16  | +30.36%               |    2,030,979,025 |   1,557,991,757 |        29.38  | -4.80%             |     69,127,947 |    50,485,798 |   781,235,173,278 |
| 0669.HK  |                 |               | 2026-07-17   | 2026-07-16  | +29.59%               |      746,098,517 |     575,721,070 |       128.3   | -1.00%             |      5,815,265 |     4,442,292 |   234,518,092,558 |
| 9961.HK  |                 |               | 2026-07-17   | 2026-07-16  | -29.37%               |      861,423,918 |   1,219,618,638 |       338.4   | -1.11%             |      2,545,579 |     3,564,052 |   213,092,243,281 |
| 1299.HK  |                 |               | 2026-07-17   | 2026-07-16  | -29.26%               |    1,535,206,811 |   2,170,262,068 |        75.55  | -0.72%             |     20,320,407 |    28,518,556 |   778,555,292,982 |
| 0975.HK  |                 |               | 2026-07-17   | 2026-07-16  | +28.84%               |       50,714,258 |      39,360,721 |         6.82  | -13.01%            |      7,436,108 |     5,020,500 |     6,977,107,646 |
| 0136.HK  | CHINA RUYI      | 中国儒意          | 2026-07-17   | 2026-07-16  | -27.66%               |      195,580,286 |     270,377,141 |         1.42  | -6.58%             |    137,732,600 |   177,879,700 |    22,074,163,255 |
| 0200.HK  | MELCO INT'L DEV | 新濠国际发展        | 2026-07-17   | 2026-07-16  | +27.59%               |       15,412,680 |      12,079,581 |         3.24  | -2.70%             |      4,757,000 |     3,627,502 |     7,370,716,926 |
| 0005.HK  | HSBC HOLDINGS   | 汇丰控股          | 2026-07-17   | 2026-07-16  | +27.02%               |    2,770,325,924 |   2,180,959,809 |       156.9   | +0.00%             |     17,656,635 |    13,900,318 | 2,690,553,966,670 |
| 9999.HK  |                 |               | 2026-07-17   | 2026-07-16  | +26.53%               |    2,440,731,702 |   1,929,031,261 |       202.8   | -0.88%             |     12,035,166 |     9,428,305 |   649,213,708,716 |
| 3328.HK  |                 |               | 2026-07-17   | 2026-07-16  | -26.36%               |      125,349,982 |     170,209,813 |         6.97  | +1.16%             |     17,984,216 |    24,703,892 |   615,895,557,494 |
| 1211.HK  |                 |               | 2026-07-17   | 2026-07-16  | -25.38%               |    2,344,839,857 |   3,142,233,355 |        88.7   | -2.47%             |     26,435,625 |    34,549,021 |   808,695,396,192 |
| 0101.HK  | HANG LUNG PPT   | 恒隆地产          | 2026-07-17   | 2026-07-16  | -24.44%               |       58,238,184 |      77,070,415 |         7.57  | -0.13%             |      7,693,287 |    10,167,601 |    39,387,335,630 |
| 0386.HK  |                 |               | 2026-07-17   | 2026-07-16  | -24.33%               |      774,701,140 |   1,023,843,828 |         4.26  | +0.47%             |    181,854,718 |   241,472,614 |   514,544,145,418 |
| 3690.HK  |                 |               | 2026-07-17   | 2026-07-16  | -24.31%               |    6,626,161,632 |   8,753,908,111 |        83.65  | -4.07%             |     79,212,929 |   100,388,858 |   516,274,522,618 |
| 1361.HK  |                 |               | 2026-07-17   | 2026-07-16  | +23.92%               |       19,601,311 |      15,817,360 |         4.53  | -0.22%             |      4,327,000 |     3,484,000 |     9,819,599,914 |
| 2020.HK  |                 |               | 2026-07-17   | 2026-07-16  | -21.86%               |      611,307,072 |     782,294,350 |        74.15  | +0.47%             |      8,244,195 |    10,600,194 |   205,432,548,603 |
| 0267.HK  |                 |               | 2026-07-17   | 2026-07-16  | +21.76%               |      159,326,206 |     130,856,014 |        11.3   | +0.00%             |     14,099,664 |    11,580,178 |   328,719,973,267 |
| 1780.HK  |                 | 荣尊国际控股        | 2026-07-17   | 2026-07-16  | -21.69%               |       18,753,651 |      23,947,201 |         3.14  | +9.03%             |      5,972,500 |     8,315,000 |     1,946,800,065 |
| 2388.HK  |                 |               | 2026-07-17   | 2026-07-16  | -21.25%               |      314,380,083 |     399,201,341 |        46.5   | -0.39%             |      6,760,862 |     8,551,871 |   491,634,282,369 |
| 9988.HK  |                 |               | 2026-07-17   | 2026-07-16  | -21.21%               |   14,147,551,366 |  17,956,875,735 |       112.6   | -3.68%             |    125,644,330 |   153,608,858 | 2,159,102,477,101 |
| 0008.HK  | PCCW            | 电讯盈科          | 2026-07-17   | 2026-07-16  | -20.92%               |       24,101,727 |      30,477,993 |         5.71  | -0.87%             |      4,220,968 |     5,291,318 |    44,239,724,273 |
| 2018.HK  |                 |               | 2026-07-17   | 2026-07-16  | -20.66%               |      309,883,251 |     390,587,949 |        38.64  | -5.85%             |      8,019,753 |     9,517,250 |    43,748,727,751 |
| 2828.HK  |                 |               | 2026-07-17   | 2026-07-16  | +20.36%               |   10,643,391,131 |   8,843,308,260 |        83.7   | -2.17%             |    127,161,189 |   103,357,977 |                   |
| 0001.HK  | CKH HOLDINGS    | 长和            | 2026-07-17   | 2026-07-16  | -20.13%               |      393,092,945 |     492,140,360 |        70.8   | +0.50%             |      5,552,160 |     6,985,669 |   271,167,162,288 |

[Download CSV report](reports/hk_volume_alerts_20260717.csv) · [Download XLSX report](reports/hk_volume_alerts_20260717.xlsx)

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
