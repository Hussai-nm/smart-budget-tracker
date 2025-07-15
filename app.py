import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.budget import (
    add_income,
    add_expense,
    get_summary,
    get_category_breakdown,
    clear_data,
    load_data,
)

st.title("Smart Budget Tracker")

# Show summary metrics
summary = get_summary()
st.markdown("### Budget Summary")
col1, col2, col3 = st.columns(3)
col1.metric("Total Income", f"${summary['income']}")
col2.metric("Total Expenses", f"${summary['expenses']}")
col3.metric("Balance", f"${summary['balance']}")

# Sidebar - Add entries
st.sidebar.header("Add Entry")
entry_type = st.sidebar.selectbox("Type", ["Income", "Expense"])

if entry_type == "Income":
    source = st.sidebar.text_input("Source")
    amount = st.sidebar.number_input("Amount", min_value=0.0)
    date = st.sidebar.date_input("Date")
    if st.sidebar.button("Add Income"):
        add_income(source, amount, str(date))
        st.sidebar.success("Income added.")
else:
    category = st.sidebar.text_input("Category")
    amount = st.sidebar.number_input("Amount", min_value=0.0)
    description = st.sidebar.text_input("Description")
    date = st.sidebar.date_input("Date")
    if st.sidebar.button("Add Expense"):
        add_expense(category, amount, description, str(date))
        st.sidebar.success("Expense added.")

# Load all data as a DataFrame
data = load_data()
df = pd.DataFrame(data)

# Show the full table if any data
if not df.empty:
    st.subheader("All Transactions")
    st.dataframe(df)

    # Add CSV download
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download as CSV",
        data=csv,
        file_name='budget_data.csv',
        mime='text/csv'
    )

    # Show category breakdown pie chart
    category_data = get_category_breakdown()
    if category_data:
        st.subheader("Expense Breakdown by Category")
        fig, ax = plt.subplots()
        ax.pie(category_data.values(), labels=category_data.keys(), autopct="%1.1f%%", startangle=90)
        ax.axis("equal")
        st.pyplot(fig)

# Clear all data
st.subheader("Reset Data")
if st.button("Clear All Data", type="primary"):
    clear_data()
    st.success("All budget data has been cleared.")
