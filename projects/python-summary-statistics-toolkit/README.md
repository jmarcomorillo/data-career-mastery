# Python Summary Statistics Toolkit

## Overview

Python Summary Statistics Toolkit is a lightweight console project that calculates basic statistics for multiple numeric datasets. It demonstrates how reusable functions can make analysis logic cleaner, easier to test, and easier to extend.

## Problem Statement

Small datasets are often summarized repeatedly using the same calculations: count, total, average, minimum, maximum, and range. This project turns those repeated calculations into reusable Python functions.

## Skills Demonstrated

- Python functions
- Parameters and return values
- Lists and dictionaries
- For loops
- Basic summary statistics
- Empty-list handling
- Reusable helper functions
- Clean console output

## Tools Used

- Python 3

## How To Run

From this project folder, run:

```bash
python summary_statistics.py
```

If Python is not available as `python`, use your local Python executable or run the script from an editor such as VS Code.

## Sample Output

```text
Python Summary Statistics Toolkit
==================================
Dataset: Daily Study Minutes
Count: 5
Total: 300
Average: 60.0
Minimum: 30
Maximum: 90
Range: 60
Average Label: Moderate
--------------------------------
```

## Results

The script summarizes three datasets:

- Daily study minutes
- Weekly expenses
- Quiz scores

Each dataset is processed through the same reusable functions, showing how functions reduce repeated code and make analysis more consistent.

## Why Empty Lists Are Handled

`sum([])` returns `0`, but `min([])` and `max([])` raise an error because there is no smallest or largest value in an empty dataset. This toolkit returns `None` for calculations where no valid result exists.

## What I Learned

This project reinforced the difference between printing a value and returning a value. Returning values makes functions reusable across different parts of a script, which is important for analysis workflows.

## Next Improvements

- Add user input for custom datasets
- Format averages to two decimal places
- Add median and standard deviation
- Export summaries to CSV
- Add automated tests
