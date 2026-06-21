"""Python Budget Category Analyzer.

A lightweight console program that summarizes expenses by category and checks
whether total spending is within a defined budget limit.
"""

expenses = [
    {"category": "Food", "amount": 250},
    {"category": "Transport", "amount": 180},
    {"category": "Utilities", "amount": 320},
    {"category": "Rent", "amount": 400},
    {"category": "Subscriptions", "amount": 150},
]

budget_limit = 1000

total_expenses = 0
highest_expense = expenses[0]
lowest_expense = expenses[0]

print("Python Budget Category Analyzer")
print("=" * 31)

for expense in expenses:
    print(f"{expense['category']}: ${expense['amount']}")
    total_expenses += expense["amount"]

    if expense["amount"] > highest_expense["amount"]:
        highest_expense = expense

    if expense["amount"] < lowest_expense["amount"]:
        lowest_expense = expense

average_expense = total_expenses / len(expenses)

print()
print(f"Total Expenses: ${total_expenses}")
print(f"Average Expense: ${average_expense}")
print(f"Highest Expense: {highest_expense['category']} - ${highest_expense['amount']}")
print(f"Lowest Expense: {lowest_expense['category']} - ${lowest_expense['amount']}")
print(f"Budget Limit: ${budget_limit}")

if total_expenses > budget_limit:
    over_budget = total_expenses - budget_limit
    print(f"Status: Over Budget by ${over_budget}")
else:
    remaining_budget = budget_limit - total_expenses
    print(f"Status: Within Budget with ${remaining_budget} remaining")
