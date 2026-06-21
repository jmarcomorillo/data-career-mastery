"""Python Summary Statistics Toolkit.

A small reusable toolkit for calculating basic summary statistics across
multiple numeric datasets.
"""


def count_values(numbers):
    """Return the number of values in a dataset."""
    return len(numbers)


def total_values(numbers):
    """Return the total of all values in a dataset."""
    return sum(numbers)


def average_value(numbers):
    """Return the average value, or None when the dataset is empty."""
    if len(numbers) == 0:
        return None
    return sum(numbers) / len(numbers)


def minimum_value(numbers):
    """Return the minimum value, or None when the dataset is empty."""
    if len(numbers) == 0:
        return None
    return min(numbers)


def maximum_value(numbers):
    """Return the maximum value, or None when the dataset is empty."""
    if len(numbers) == 0:
        return None
    return max(numbers)


def value_range(numbers):
    """Return the range, or None when the dataset is empty."""
    if len(numbers) == 0:
        return None
    return max(numbers) - min(numbers)


def average_label(numbers):
    """Label a dataset as Low, Moderate, High, or Not Available."""
    average = average_value(numbers)

    if average is None:
        return "Not Available"
    if average < 50:
        return "Low"
    if average < 100:
        return "Moderate"
    return "High"


def print_dataset_summary(dataset_name, values):
    """Print a clean summary for one dataset."""
    print(f"Dataset: {dataset_name}")
    print(f"Count: {count_values(values)}")
    print(f"Total: {total_values(values)}")
    print(f"Average: {average_value(values)}")
    print(f"Minimum: {minimum_value(values)}")
    print(f"Maximum: {maximum_value(values)}")
    print(f"Range: {value_range(values)}")
    print(f"Average Label: {average_label(values)}")
    print("-" * 32)


datasets = {
    "Daily Study Minutes": [60, 30, 90, 45, 75],
    "Weekly Expenses": [250, 180, 320, 400, 150],
    "Quiz Scores": [82, 91, 76, 88, 95],
}

print("Python Summary Statistics Toolkit")
print("=" * 34)

for name, values in datasets.items():
    print_dataset_summary(name, values)
