import sys
import os
sys.path.insert(0, 'financial_analysis')
from check_requirements import check_packages
check_packages()

from config import DATA_FOLDER, IGNORED_CATEGORIES, CATEGORIZATION_RULES
from reader import load_csv
from normalizer import normalize
from cleaner import clean_transactions
from analyzer import summarize_by_category, monthly_spending
from categorizer import categorize_transactions
from visualizer import plot_summary_by_category, plot_monthly_spending

import pandas as pd

def main():
    all_data = []

    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(script_dir, DATA_FOLDER)
    csv_files = [f for f in os.listdir(data_dir) if f.endswith(".csv")]

    for filename in csv_files:
        file_path = os.path.join(data_dir, filename)
        raw_df = load_csv(file_path)
        norm_df = normalize(raw_df, filename)
        clean_df = clean_transactions(norm_df, IGNORED_CATEGORIES)
        all_data.append(clean_df)

    merged = pd.concat(all_data, ignore_index=True)
    merged = categorize_transactions(merged, CATEGORIZATION_RULES)

    summary = summarize_by_category(merged)
    print("\n--- Summary by Category ---")
    print(summary)
    plot_summary_by_category(summary)

    monthly = monthly_spending(merged)
    print("\n--- Monthly Spending ---")
    print(monthly)
    plot_monthly_spending(monthly)

    merged.to_csv(os.path.join(script_dir, "financial_analysis/cleaned_transactions.csv"), index=False)

if __name__ == "__main__":
    main()
