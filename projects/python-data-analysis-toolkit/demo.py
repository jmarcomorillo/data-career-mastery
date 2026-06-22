"""Demonstration script for the Python Data Analysis Toolkit."""

import csv
from pathlib import Path

from toolkit import (
    DatasetSummary,
    check_budget,
    format_number,
    summarize_groups,
)


DATA_PATH = Path(__file__).parent / "data" / "ds_salaries_ph.csv"


def load_salary_records(file_path=DATA_PATH):
    """Load salary records from a local CSV file."""
    records = []

    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                salary = int(row["Salary"])
            except (KeyError, TypeError, ValueError):
                continue

            records.append(
                {
                    "work_year": row.get("Work Year"),
                    "seniority": row.get("Seniority"),
                    "employee_status": row.get("Employee Status"),
                    "position": row.get("Job Role"),
                    "salary": salary,
                    "company_size": row.get("Company Size"),
                }
            )

    return records


def print_group_summary_table(group_summaries, title, limit=10):
    """Print a compact table of category summaries."""
    print(title)
    print("-" * len(title))
    print(f"{'Category':35} {'Count':>5} {'Average':>12} {'Min':>12} {'Max':>12}")

    for summary in group_summaries[:limit]:
        print(
            f"{summary['name'][:35]:35} "
            f"{summary['count']:>5} "
            f"{format_number(summary['average']):>12} "
            f"{format_number(summary['minimum']):>12} "
            f"{format_number(summary['maximum']):>12}"
        )

    print()


def main():
    salary_records = load_salary_records()
    salaries = [record["salary"] for record in salary_records]

    print("Python Data Analysis Toolkit")
    print("=" * 28)
    print(f"Loaded records: {len(salary_records)}")
    print(f"Data file: {DATA_PATH.name}")
    print()

    overall_summary = DatasetSummary("Overall Salary", salaries)
    overall_summary.print_summary()

    salary_budget = 200_000_000
    budget_result = check_budget(overall_summary.total(), salary_budget)
    print(f"Budget Limit: {format_number(salary_budget)}")
    print(f"Budget Status: {budget_result['message']}")
    print()

    position_summaries = summarize_groups(salary_records, "position", "salary")
    position_summaries = sorted(
        position_summaries,
        key=lambda summary: summary["average"] or 0,
        reverse=True,
    )

    print_group_summary_table(
        position_summaries,
        "Top Positions by Average Salary",
        limit=10,
    )


if __name__ == "__main__":
    main()
