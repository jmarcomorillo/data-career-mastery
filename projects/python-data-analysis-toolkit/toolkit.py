"""Reusable helpers for small Python data analysis projects."""

from collections import defaultdict


def count_values(numbers):
    """Return the number of values in a numeric list."""
    return len(numbers)


def total_values(numbers):
    """Return the total of a numeric list."""
    return sum(numbers)


def average_value(numbers):
    """Return the average of a numeric list, or None when empty."""
    if len(numbers) == 0:
        return None
    return sum(numbers) / len(numbers)


def minimum_value(numbers):
    """Return the minimum value, or None when empty."""
    if len(numbers) == 0:
        return None
    return min(numbers)


def maximum_value(numbers):
    """Return the maximum value, or None when empty."""
    if len(numbers) == 0:
        return None
    return max(numbers)


def value_range(numbers):
    """Return max minus min, or None when empty."""
    if len(numbers) == 0:
        return None
    return max(numbers) - min(numbers)


def format_number(value):
    """Format numbers for reports while preserving unavailable values."""
    if value is None:
        return "N/A"
    if isinstance(value, float):
        return f"{value:,.2f}"
    return f"{value:,}"


class DatasetSummary:
    """Summarize a named numeric dataset."""

    def __init__(self, name, values):
        self.name = name
        self.values = values

    def count(self):
        return count_values(self.values)

    def total(self):
        return total_values(self.values)

    def average(self):
        return average_value(self.values)

    def minimum(self):
        return minimum_value(self.values)

    def maximum(self):
        return maximum_value(self.values)

    def value_range(self):
        return value_range(self.values)

    def as_dict(self):
        """Return summary values as a dictionary."""
        return {
            "name": self.name,
            "count": self.count(),
            "total": self.total(),
            "average": self.average(),
            "minimum": self.minimum(),
            "maximum": self.maximum(),
            "range": self.value_range(),
        }

    def print_summary(self):
        """Print a clean text report for the dataset."""
        summary = self.as_dict()
        print(f"Summary: {summary['name']}")
        print(f"Count:   {format_number(summary['count'])}")
        print(f"Total:   {format_number(summary['total'])}")
        print(f"Average: {format_number(summary['average'])}")
        print(f"Minimum: {format_number(summary['minimum'])}")
        print(f"Maximum: {format_number(summary['maximum'])}")
        print(f"Range:   {format_number(summary['range'])}")
        print("-" * 40)


def summarize_numeric_dataset(name, values):
    """Return a DatasetSummary object for a numeric dataset."""
    return DatasetSummary(name, values)


def group_values_by_category(records, category_key, value_key):
    """Group numeric values by a category key."""
    grouped_values = defaultdict(list)

    for record in records:
        category = record.get(category_key)
        value = record.get(value_key)

        if category is not None and value is not None:
            grouped_values[category].append(value)

    return dict(grouped_values)


def summarize_groups(records, category_key, value_key):
    """Return summary dictionaries for every category group."""
    grouped_values = group_values_by_category(records, category_key, value_key)
    summaries = []

    for category, values in grouped_values.items():
        summary = DatasetSummary(category, values).as_dict()
        summaries.append(summary)

    return summaries


def check_budget(total, budget_limit):
    """Return budget status details for a total and limit."""
    difference = budget_limit - total

    if difference >= 0:
        return {
            "status": "Within Budget",
            "difference": difference,
            "message": f"Within Budget with {format_number(difference)} remaining",
        }

    return {
        "status": "Over Budget",
        "difference": abs(difference),
        "message": f"Over Budget by {format_number(abs(difference))}",
    }
