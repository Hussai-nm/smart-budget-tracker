# Smart Budget Tracker

Smart Budget Tracker is a simple and interactive budget tracking app built with Python and Streamlit. It allows you to add income and expenses, view summaries, and download your transaction history as a CSV file.

## Features

- Add income and expenses via a sidebar interface
- View all transactions in a table
- Breakdown of expenses by category
- Summary showing total income, expenses, and balance
- Download all transactions as a CSV file
- Local data storage using JSON

## Project Structure

smart-budget-tracker/
├── app.py # Streamlit UI
├── test.py # Test script for logic
├── src/
│ ├── init.py
│ └── budget.py # Core budget functionality
├── data/
│ └── budget_data.json # Local data store (created automatically)
├── requirements.txt # Python dependencies
└── .gitignore



## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Hussai-nm/smart-budget-tracker.git
   cd smart-budget-tracker

python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py

## Example Usage

1. Use the sidebar to add income or expenses.
2. Fill in the relevant fields such as source, amount, category, description, and date.
3. View the full transaction table and a summary of your financial data.
4. Download the data as a CSV for your own records.

## Dev Notes

- `test.py` is a developer script used to manually test the budget functions. It is not part of the user-facing interface.


## Notes

- All data is stored locally in the data/budget_data.json file.
- No external database or cloud storage is used.


## License

This project is licensed under the MIT License.
