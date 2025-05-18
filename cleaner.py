import pandas as pd

def clean_transactions(df, ignored_categories):
    df = df.drop_duplicates()
    df = df[~df["Description"].str.contains('|'.join(ignored_categories), case=False, na=False)]
    df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")
    df = df.dropna(subset=["Date", "Amount"])
    return df
