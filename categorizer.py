import pandas as pd
from config import RULES_FILE

def categorize_transactions(df, rules, rules_path=RULES_FILE):
    df["Category"] = "Uncategorized"

    # Apply existing rules
    for category, keywords in rules.items():
        mask = df["Description"].str.lower().str.contains('|'.join(keywords), na=False)
        df.loc[mask, "Category"] = category

    # Identify uncategorized transactions
    uncategorized = df[df["Category"] == "Uncategorized"]
    if uncategorized.empty:
        return df

    new_rules = []

    # Prompt user for review mode
    print(f"\n{len(uncategorized)} uncategorized transactions found.")
    use_batch = input("Would you like to review them all at once? (y/n): ").strip().lower() == 'y'

    if use_batch:
        print("\nUncategorized Transactions:")
        for i, (_, row) in enumerate(uncategorized.iterrows()):
            print(f"[{i}] \"{row['Description']}\"")

        for i, (idx, row) in enumerate(uncategorized.iterrows()):
            prompt = f"Enter category for [{i}] ({row['Description']}): "
            user_input = input(prompt).strip()
            if user_input:
                df.at[idx, "Category"] = user_input
                new_rules.append({"Category": user_input, "Keyword": row["Description"].lower(), "Ignore": 0})
    else:
        for idx, row in uncategorized.iterrows():
            desc = row["Description"]
            print(f"\nUncategorized transaction: {desc}")
            user_input = input("Enter a category for this transaction (or press Enter to skip): ").strip()
            if user_input:
                df.at[idx, "Category"] = user_input
                new_rules.append({"Category": user_input, "Keyword": desc.lower(), "Ignore": 0})

    # Append new rules to the CSV file if any
    if new_rules:
        new_df = pd.DataFrame(new_rules)
        try:
            existing = pd.read_csv(rules_path)
            updated = pd.concat([existing, new_df], ignore_index=True)
            updated.drop_duplicates(subset=["Keyword"], inplace=True)
        except FileNotFoundError:
            updated = new_df

        updated.to_csv(rules_path, index=False)

    return df
