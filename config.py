import pandas as pd
import os

WORKING_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_FOLDER = os.path.join(WORKING_DIR, "source_data")
RULES_FILE = os.path.join(WORKING_DIR, "data", "category_rules.csv")
OUTPUT_FILE = os.path.join(WORKING_DIR, "cleaned_transactions.csv")

STANDARD_COLUMNS = ["Date", "Description", "Amount", "Category", "Institution"]

def load_rules(csv_path=RULES_FILE):
    df = pd.read_csv(csv_path)
    categorized = df[df["Ignore"] == 0]
    ignored = df[df["Ignore"] == 1]["Keyword"].dropna().tolist()

    categorization_rules = {}
    for category, group in categorized.groupby("Category"):
        categorization_rules[category] = group["Keyword"].dropna().tolist()
    return categorization_rules, ignored

CATEGORIZATION_RULES, IGNORED_CATEGORIES = load_rules()
