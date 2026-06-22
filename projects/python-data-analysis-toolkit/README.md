# Python Data Analysis Toolkit

## Overview

Python Data Analysis Toolkit is a reusable standard-library Python project for summarizing numeric datasets and category-based records. It demonstrates core Python foundations through a practical salary dataset example.

## Problem Statement

Raw salary records are difficult to review directly. This project builds a small toolkit that can calculate overall summary statistics, group records by category, and produce readable report output.

## Dataset

The demo uses `ds_salaries_ph.csv`, a Philippine data salary dataset downloaded from Kaggle:

```text
https://www.kaggle.com/datasets/kendricmontero/data-salaries-ph
```

Each row represents a salary record with columns such as work year, seniority, employee status, job role, salary, and company size.

The salary column is analyzed as provided in the dataset. This project does not yet normalize salary units, remove outliers, or perform advanced cleaning.

## Skills Demonstrated

- CSV loading with Python's standard library
- Numeric summary functions
- Empty-list handling with `None`
- Category grouping
- Budget checking
- Object-oriented programming with a `DatasetSummary` class
- Clean report output
- Portable local file paths with `pathlib`

## Tools Used

- Python 3
- Standard library modules: `csv`, `pathlib`, `collections`

## Project Structure

```text
python-data-analysis-toolkit/
  data/
    ds_salaries_ph.csv
  toolkit.py
  demo.py
  README.md
  REFLECTION.md
  .gitignore
```

## How To Run

From this project folder, run:

```bash
python demo.py
```

If Python is not available as `python`, use your local Python executable or run the script from an editor such as VS Code.

## Features

- Count values
- Calculate totals
- Calculate averages
- Find minimum and maximum values
- Calculate range
- Summarize records by category
- Check a total against a budget limit
- Print clean summary reports

## Sample Output

```text
Python Data Analysis Toolkit
============================
Loaded records: 607
Data file: ds_salaries_ph.csv

Summary: Overall Salary
Count:   607
Total:   196,668,038
Average: 324,000.06
Minimum: 4,000
Maximum: 30,400,000
Range:   30,396,000
----------------------------------------
```

## Results

The toolkit loads salary records, summarizes overall salary values, checks the salary total against a sample budget limit, and prints the top positions by average salary.

## Notes

This project focuses on Python foundations rather than advanced data analysis. Later projects will use Pandas, visualization, statistics, and deeper exploratory analysis.

## Next Improvements

- Add command-line options
- Export summaries to CSV
- Add tests for toolkit functions
- Add more category summaries, such as seniority and company size
- Build a Pandas version in a later project
