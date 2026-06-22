"""Python Dataset Summary Class.

A compact object-oriented example for summarizing numeric datasets with a
reusable class.
"""


class DatasetSummary:
    """Store a dataset name and values, then calculate summary statistics."""

    def __init__(self, name, values):
        self.name = name
        self.values = values

    def count(self):
        """Return the number of values."""
        return len(self.values)

    def total(self):
        """Return the sum of values."""
        return sum(self.values)

    def average(self):
        """Return the average value, or None when the dataset is empty."""
        if len(self.values) == 0:
            return None
        return sum(self.values) / len(self.values)

    def minimum(self):
        """Return the minimum value, or None when the dataset is empty."""
        if len(self.values) == 0:
            return None
        return min(self.values)

    def maximum(self):
        """Return the maximum value, or None when the dataset is empty."""
        if len(self.values) == 0:
            return None
        return max(self.values)

    def value_range(self):
        """Return the range, or None when the dataset is empty."""
        if len(self.values) == 0:
            return None
        return self.maximum() - self.minimum()

    def average_label(self):
        """Label the dataset based on its average value."""
        average = self.average()

        if average is None:
            return "Not Available"
        if average >= 75:
            return "High"
        if average >= 50:
            return "Moderate"
        return "Low"

    def summary(self):
        """Print a clean dataset summary."""
        print(f"Dataset: {self.name}")
        print(f"Count: {self.count()}")
        print(f"Total: {self.total()}")
        print(f"Average: {self.average()}")
        print(f"Average Label: {self.average_label()}")
        print(f"Minimum: {self.minimum()}")
        print(f"Maximum: {self.maximum()}")
        print(f"Range: {self.value_range()}")
        print("-" * 32)


study_minutes = DatasetSummary("Daily Study Minutes", [60, 30, 90, 45, 75])
quiz_scores = DatasetSummary("Quiz Scores", [82, 91, 76, 88, 95])
weekly_expenses = DatasetSummary("Weekly Expenses", [])

print("Python Dataset Summary Class")
print("=" * 28)

study_minutes.summary()
quiz_scores.summary()
weekly_expenses.summary()
