import os
import json
import pandas as pd
from config import WORKING_DIR
from normalizer import normalize_dataframe, load_mapping
from categorizer import categorize_transactions
from analyzer import monthly_spending
from visualizer import plot_monthly_spending, plot_summary_by_category

# Define paths
SOURCE_DATA_DIR = os.path.join(WORKING_DIR, "source_data")
NORMALIZED_DATA_DIR = os.path.join(WORKING_DIR, "normalized")
INSTITUTION_MAP_PATH = os.path.join(WORKING_DIR, "data", "institution_names.json")
os.makedirs(NORMALIZED_DATA_DIR, exist_ok=True)

def detect_source_name(file_name):
    for name in ["CHCC", "GFCU", "PP"]:
        if name in file_name.upper():
            return name
    return None

def main():
    all_data = []

    with open(INSTITUTION_MAP_PATH, "r") as f:
        institution_map = json.load(f)

    for file in os.listdir(SOURCE_DATA_DIR):
        if file.lower().endswith(".csv"):
            file_path = os.path.join(SOURCE_DATA_DIR, file)
            source = detect_source_name(file)
            if not source:
                print(f"Skipping {file}: unable to detect source.")
                continue
            try:
                df = pd.read_csv(file_path, encoding="utf-8")
                df.columns = df.columns.str.strip()
                mapping = load_mapping(source)
                df_normalized = normalize_dataframe(df, mapping)
                df_normalized["institution"] = institution_map.get(source, source)

                out_path = os.path.join(NORMALIZED_DATA_DIR, f"normalized_{source}.csv")
                df_normalized.to_csv(out_path, index=False)
                print(f"Normalized: {file} -> {out_path}")

                all_data.append(df_normalized)
            except Exception as e:
                print(f"Error processing {file}: {e}")
                try:
                    print("Available columns:", pd.read_csv(file_path, encoding="utf-8").columns.tolist())
                except Exception as inner_e:
                    print("Could not read columns due to:", inner_e)

    if all_data:
        merged_df = pd.concat(all_data, ignore_index=True)
        categorized_df = categorize_transactions(merged_df, {})

        monthly_df = monthly_spending(categorized_df)
        plot_monthly_spending(monthly_df)
        plot_spending_by_category(categorized_df)

        final_output_path = os.path.join(WORKING_DIR, "final_categorized_transactions.csv")
        categorized_df.to_csv(final_output_path, index=False)
        print(f"Final categorized data saved to {final_output_path}")

if __name__ == "__main__":
    main()
