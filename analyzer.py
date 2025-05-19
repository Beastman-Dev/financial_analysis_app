import pandas as pd

def summarize_by_category(df):
    amt_col = "Amount" if "Amount" in df.columns else "amount"
    return (
        df.groupby("Category")[amt_col]
          .sum()
          .sort_values(ascending=False)
    )

def monthly_spending(df):
    # 1) find the date column
    if "Date" in df.columns:
        date_col = "Date"
    elif "date" in df.columns:
        date_col = "date"
    else:
        raise KeyError("No 'Date' or 'date' column found for monthly_spending()")

    # 2) find the amount column
    if "Amount" in df.columns:
        amt_col = "Amount"
    elif "amount" in df.columns:
        amt_col = "amount"
    else:
        raise KeyError("No 'Amount' or 'amount' column found for monthly_spending()")

    # 3) coerce to datetime and extract month
    df["Date"] = pd.to_datetime(df[date_col], errors="coerce")
    df["Month"] = df["Date"].dt.to_period("M")

    # 4) group and return
    return df.groupby("Month")[amt_col].sum()
