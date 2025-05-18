import pandas as pd

STANDARD_COLUMNS = ["Date", "Description", "Amount", "Category", "Institution"]

DATA_FOLDER = "sample_data"

def load_rules(csv_path="financial_analysis/data/category_rules.csv"):
    df = pd.read_csv(csv_path)
    categorized = df[df["Ignore"] == 0]
    ignored = df[df["Ignore"] == 1]["Keyword"].dropna().tolist()

    categorization_rules = {}
    for category, group in categorized.groupby("Category"):
        categorization_rules[category] = group["Keyword"].dropna().tolist()
    return categorization_rules, ignored

CATEGORIZATION_RULES, IGNORED_CATEGORIES = load_rules()