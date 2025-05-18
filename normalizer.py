def normalize(df, institution):
    mapping = {
        "institution_1.csv": {"Txn Date": "Date", "Details": "Description", "Amount USD": "Amount"},
        "institution_2.csv": {"Date": "Date", "Memo": "Description", "Value": "Amount"},
    }

    if institution in mapping:
        df = df.rename(columns=mapping[institution])

    df["Institution"] = institution

    return df[["Date", "Description", "Amount", "Institution"]]