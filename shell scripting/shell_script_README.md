# Shell Script Assignment - Company Data Extraction

## Overview

The script fetches S&P 500 company data from a remote CSV file, extracts relevant columns, sorts by founding year, and outputs formatted results.

---

## Script Details

**File:** `info.sh`

**Purpose:** Extract and sort company information by founding year from a CSV dataset

**Input:** URL to a CSV file containing company data

**Output:** Company name, headquarters location, and founding year (sorted by year, oldest first)

---

## Requirements

The script requires the following tools to be installed:

- `bash` - Shell interpreter
- `curl` - For fetching remote files
- `csvkit` - For CSV processing (`csvcut`, `csvsort`)
  - Install: `pip install csvkit`
- `awk` - For text formatting (usually pre-installed)

---

## Usage

### Make the script executable:

```bash
chmod +x info.sh
```

### Run the script:

```bash
./info.sh <csv_url>
```

### Example:

```bash
./info.sh https://raw.githubusercontent.com/datasets/s-and-p-500-companies/refs/heads/main/data/constituents.csv
```

---

## Sample Output

```
BNY Mellon, "New York City, New York", 1784
Berkshire Hathaway, "Omaha, Nebraska", 1839
American Express, "New York City, New York", 1850
Ball Corporation, "Broomfield, Colorado", 1880
American Water Works, "Camden, New Jersey", 1886
Abbott Laboratories, "North Chicago, Illinois", 1888
Assurant, "Atlanta, Georgia", 1892
Ameriprise Financial, "Minneapolis, Minnesota", 1894
Becton Dickinson, "Franklin Lakes, New Jersey", 1897
3M, "Saint Paul, Minnesota", 1902
...
```

---

## How It Works

The script performs the following operations in a pipeline:

1. **Fetch data**: `curl -s "$URL"` downloads the CSV file
2. **Extract columns**: `csvcut` selects "Security", "Headquarters Location", and "Founded" columns
3. **Sort**: `csvsort` orders results by the "Founded" column (chronologically)
4. **Remove header**: `tail -n +2` skips the CSV header row
5. **Format output**: `awk` prints comma-separated values in readable format

---

## Technical Notes

### Encoding Handling

The script uses `--encoding latin1` for the `csvcut` command to handle the UTF-8 BOM (Byte Order Mark) present in the source CSV file. This prevents encoding errors while processing the data.
