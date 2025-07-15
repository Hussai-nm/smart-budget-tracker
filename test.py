from src.budget import add_income, add_expense, get_summary, get_category_breakdown
from src.budget import clear_data
add_income("Freelance", 800, "2025-07-15")
add_expense("Food", 50, "Lunch with friends", "2025-07-15")

summary = get_summary()
print("\n Budget Summary:")
print(f"  Total Income: ${summary['total_income']}")
print(f"  Total Expenses: ${summary['total_expense']}")
print(f"  Balance: ${summary['balance']}")

breakdown = get_category_breakdown()
print("\n Category Breakdown:")
for category, total in breakdown.items():
    print(f"  {category}: ${total}")


clear_data()
