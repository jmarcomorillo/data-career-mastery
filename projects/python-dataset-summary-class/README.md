# Python Dataset Summary Class

## Overview

Python Dataset Summary Class is a compact object-oriented programming project that summarizes numeric datasets through a reusable class. It demonstrates how data and related behavior can be grouped together inside a class.

## Problem Statement

Dataset summaries often require the same calculations: count, total, average, minimum, maximum, and range. This project organizes those calculations inside a `DatasetSummary` class so each dataset object can summarize itself consistently.

## Skills Demonstrated

- Object-oriented programming basics
- Class creation
- Object creation
- `__init__`
- Attributes with `self`
- Methods
- Empty-list handling
- Reusable summary behavior
- Clean console output

## Tools Used

- Python 3

## How To Run

From this project folder, run:

```bash
python dataset_summary.py
```

If Python is not available as `python`, use your local Python executable or run the script from an editor such as VS Code.

## Sample Output

```text
Python Dataset Summary Class
============================
Dataset: Daily Study Minutes
Count: 5
Total: 300
Average: 60.0
Average Label: Moderate
Minimum: 30
Maximum: 90
Range: 60
--------------------------------
```

## Results

The project creates three dataset objects and prints a summary for each one. It also handles an empty dataset safely by returning `None` for calculations where no valid result exists.

## Why `None` Is Used

An empty dataset has no valid minimum, maximum, average, or range. Returning `None` makes that missing result explicit without pretending that `0` is a real calculated value.

## What I Learned

This project reinforced how classes can group data and behavior together. Instead of writing separate functions and passing datasets around, each dataset object stores its own name and values, then uses methods to summarize itself.

## Next Improvements

- Add median and standard deviation methods
- Add formatted output for unavailable values
- Create a reusable module without direct print calls
- Add automated tests
- Support loading datasets from CSV files
