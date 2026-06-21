# Recall: Python Profile Tracker

## Overview

Recall is a lightweight Python console project that stores multiple learner profiles and prints a clean summary for each one. It demonstrates how basic Python data structures can represent structured records in a readable and scalable way.

## Problem Statement

Simple learning records often begin as unstructured notes. This project turns those records into structured Python dictionaries, making each learner profile easier to read, update, and eventually analyze.

## Skills Demonstrated

- Python variables
- Lists and dictionaries
- List-of-dictionaries record structure
- Boolean values
- For loops
- F-string formatting
- String joining with `.join()`
- Clean console output

## Tools Used

- Python 3

## How To Run

From this project folder, run:

```bash
python profile_tracker.py
```

If Python is not available as `python`, use your local Python executable or run the script from an editor such as VS Code.

## Sample Output

```text
Recall: Python Profile Tracker
================================
Learner: Jade
Target Role: Data Scientist
Current Skill Level: 8/10
Skills in Focus: Data Preprocessing, Exploratory Data Analysis, Data Cleaning
Study Minutes Logged: 60
Session Completed: Yes
--------------------------------
```

## Results

The script stores three learner profiles and prints a consistent summary for each profile. The final structure uses a list of dictionaries, which is a common Python pattern for representing multiple records.

## What I Learned

This project reinforced the importance of choosing the right data structure before working with information. A list of dictionaries made the data easier to loop through, print, and expand.

## Next Improvements

- Add user input for new profiles
- Validate skill level values
- Calculate total study minutes
- Save profiles to a file
- Convert the printing logic into a reusable function
