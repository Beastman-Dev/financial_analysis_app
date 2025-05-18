import pandas as pd

def summarize_by_category(df):
    return df.groupby("Category")["Amount"].sum().sort_values(ascending=False)

def monthly_spending(df):
    df["Date"] = pd.to_datetime(df["Date"])
    df["Month"] = df["Date"].dt.to_period("M")
    return df.groupby("Month")["Amount"].sum()