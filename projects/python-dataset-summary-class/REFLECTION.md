# Project Reflection

## Summary

This project introduced object-oriented programming through a practical dataset summary class. The final version stores dataset information in object attributes and uses methods to calculate summary statistics.

## Key Takeaways

- A class is a blueprint for creating objects.
- An object is an instance created from a class.
- A method is a function defined inside a class.
- `self` refers to the current object.
- `__init__` runs when a new object is created.
- `None` is useful when no valid calculation result exists.

## Improvement Notes

The first version returned `0` for empty-list calculations and used a method named `range`. The final version returns `None` for unavailable values and uses `value_range()` to avoid confusion with Python's built-in `range`.
