import json
import os
from collections import defaultdict


DATA_FILE = "data/budget_data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def add_income(source, amount, date):
    data = load_data()
    income_entry = {
        "type": "income",
        "source": source,
        "amount": amount,
        "date": date
    }
    data.append(income_entry)
    save_data(data)
    print("Income added.")

def add_expense(category, amount, description, date):
    data = load_data()
    expense_entry = {
        "type": "expense",
        "category": category,
        "amount": amount,
        "description": description,
        "date": date
    }
    data.append(expense_entry)
    save_data(data)
    print(" Expense added.")


def get_summary():
    data = load_data()
    total_income = sum(entry["amount"] for entry in data if entry["type"] == "income")
    total_expense = sum(entry["amount"] for entry in data if entry["type"] == "expense")
    balance = total_income - total_expense

    summary = {
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": balance
    }

    return summary


def get_category_breakdown():
    data = load_data()
    category_totals = defaultdict(float)

    for entry in data:
        if entry["type"] == "expense":
            category = entry["category"]
            category_totals[category] += entry["amount"]

    return dict(category_totals)

def clear_data():
    save_data([])
    print("Data has been cleared.")
