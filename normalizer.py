import pandas as pd
import json
import os
from datetime import datetime
from config import WORKING_DIR

MAPPING_DIR = os.path.join(WORKING_DIR, "mappings")


def load_mapping(source_name):
    path = os.path.join(MAPPING_DIR, f"{source_name}.json")
    if not os.path.exists(path):
        raise FileNotFoundError(f"Mapping for '{source_name}' not found at {path}")
    with open(path, "r") as f:
        return json.load(f)


def normalize_dataframe(df, mapping):
    columns = mapping.get("columns", {})
    combine = mapping.get("combine", {})
    formatting = mapping.get("formatting", {})

    # Rename columns
    df = df.rename(columns=columns)

    # Combine columns if specified (e.g., date + time)
    for target_col, parts in combine.items():
        df[target_col] = df[parts[0]].astype(str) + " " + df[parts[1]].astype(str)

    # Format date columns
    if "date" in formatting:
        fmt = formatting["date"].get("format")
        if fmt:
            df["date"] = pd.to_datetime(df["date"], format=fmt, errors='coerce')

    # Convert amount to float
    if "amount" in df.columns:
        df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

    return df[[col for col in ["date", "description", "amount", "type", "category", "notes"] if col in df.columns]]


def normalize_file(file_path, source_name):
    df = pd.read_csv(file_path)
    mapping = load_mapping(source_name)
    return normalize_dataframe(df, mapping)


# Example usage within pipeline:
# normalized_df = normalize_file(os.path.join(WORKING_DIR, "cleansed_CHCC.csv"), "CHCC")
# normalized_df.to_csv(os.path.join(WORKING_DIR, "normalized_CHCC.csv"), index=False)
