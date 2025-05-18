
def categorize_transactions(df, rules):
    df["Category"] = "Uncategorized"
    for category, keywords in rules.items():
        mask = df["Description"].str.lower().str.contains('|'.join(keywords), na=False)
        df.loc[mask, "Category"] = category
    return df
