# Python Budget Category Analyzer

## Overview

Python Budget Category Analyzer is a lightweight console project that summarizes expenses by category and checks whether total spending is within a defined budget limit.

## Problem Statement

Budget data is easier to understand when expenses are grouped by category and summarized clearly. This project analyzes a small set of expense records, calculates total and average spending, identifies the highest and lowest categories, and reports whether the budget is over or within limit.

## Skills Demonstrated

- Python lists and dictionaries
- List-of-dictionaries record structure
- For loops
- Running totals
- Conditional logic
- Highest and lowest value tracking
- Budget comparison logic
- Clean console output

## Tools Used

- Python 3

## How To Run

From this project folder, run:

```bash
python budget_analyzer.py
```

If Python is not available as `python`, use your local Python executable or run the script from an editor such as VS Code.

## Sample Output

```text
Python Budget Category Analyzer
===============================
Food: $250
Transport: $180
Utilities: $320
Rent: $400
Subscriptions: $150

Total Expenses: $1300
Average Expense: $260.0
Highest Expense: Rent - $400
Lowest Expense: Subscriptions - $150
Budget Limit: $1000
Status: Over Budget by $300
```

## Results

The script identifies that total spending is over the budget limit. It also highlights the highest expense category and the lowest expense category, making the spending pattern easier to review.

## What I Learned

This project reinforced how loops can process repeated records one at a time. It also showed how a running total and comparison variables can be used to summarize a list of dictionaries without manually calculating each value.

## Next Improvements

- Add user input for custom categories
- Format currency values consistently
- Support multiple budget limits
- Export the summary to CSV
- Add validation for missing or negative amounts
