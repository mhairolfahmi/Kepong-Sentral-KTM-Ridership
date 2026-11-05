# Kepong Sentral Station Ridership Data Pipeline

This project focuses on building a data pipeline to extract daily KTM ridership data from Malaysia's open data portal, [data.gov.my](https://data.gov.my/). The pipeline uses Python (Pandas) to transform and filter passenger journeys, including only records where the journey either begins or ends at Kepong Sentral station. The processed data is then loaded into CSV files and an SQLite database for further analysis.

## Project Objectives

- Extract daily KTM ridership data from data.gov.my.
- Validate the extracted data to check for null values, column requirement and duplicate.
- Filter passenger journeys that either begin or end at Kepong Sentral station.
- Transform and process the ridership data.
- Store the processed data in CSV files and an SQLite database.


## Tools Used

- Python (Pandas)
- SQLite
- VS Code
- Git and GitHub

## Monthly Ridership

| Month | Ridership |
|---|---:|
| January 2026 | 5,906 |
| February 2026 | 5,315 |
| March 2026 | 6,177 |
| April 2026 | 6,256 |
| May 2026 | 6,274 |
| June 2026 | 6,007 |
| July 2026 | 6,107 |
| August 2026 | 5,844 |
| September 2026 | 5,598 |
| October 2026 | 5,897 |

## Hourly Ridership

| Time | Ridership |
|---|---:|
| 00:00 | 145 |
| 01:00 | 19 |
| 02:00 | 8 |
| 03:00 | 4 |
| 04:00 | 10 |
| 05:00 | 818 |
| 06:00 | 3,497 |
| 07:00 | 4,309 |
| 08:00 | 5,151 |
| 09:00 | 5,728 |
| 10:00 | 2,381 |
| 11:00 | 3,166 |
| 12:00 | 2,474 |
| 13:00 | 1,855 |
| 14:00 | 2,024 |
| 15:00 | 2,987 |
| 16:00 | 2,353 |
| 17:00 | 3,546 |
| 18:00 | 4,714 |
| 19:00 | 6,309 |
| 20:00 | 3,250 |
| 21:00 | 2,145 |
| 22:00 | 2,032 |
| 23:00 | 456 |