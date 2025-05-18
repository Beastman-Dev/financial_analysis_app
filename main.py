from config import DATA_PATHS, IGNORED_CATEGORIES, CATEGORIZATION_RULES
from reader import load_csv
from normalizer import normalize
from cleaner import clean_transactions
from analyzer import summarize_by_category, monthly_spending
from categorizer import categorize_transactions
from visualizer import plot_summary_by_category, plot_monthly_spending

import pandas as pd

def main():
    all_data = []

    for path in DATA_PATHS:
        raw_df = load_csv("financial_analysis/" + path)
        norm_df = normalize(raw_df, path.split('/')[-1])
        clean_df = clean_transactions(norm_df, IGNORED_CATEGORIES)
        all_data.append(clean_df)

    merged = pd.concat(all_data, ignore_index=True)

    merged = categorize_transactions(merged, CATEGORIZATION_RULES)

    print("\n--- Summary by Category ---")
    print(summarize_by_category(merged))

    summary = summarize_by_category(merged)
    print("\n--- Summary by Category ---")
    print(summary)
    plot_summary_by_category(summary)

    monthly = monthly_spending(merged)
    print("\n--- Monthly Spending ---")
    print(monthly)
    plot_monthly_spending(monthly)
    print(monthly_spending(merged))

    merged.to_csv("financial_analysis/cleaned_transactions.csv", index=False)

if __name__ == "__main__":
    main()