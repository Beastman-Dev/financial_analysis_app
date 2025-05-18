import pandas as pd
import matplotlib.pyplot as plt
import os
from config import WORKING_DIR

CHART_DIR = os.path.join(WORKING_DIR, "charts")
os.makedirs(CHART_DIR, exist_ok=True)

def plot_summary_by_category(summary_df):
    summary_df.plot(kind='bar', figsize=(10, 6), title='Spending by Category')
    plt.xlabel('Category')
    plt.ylabel('Total Amount')
    plt.tight_layout()
    filepath = os.path.join(CHART_DIR, "spending_by_category.png")
    plt.savefig(filepath)
    plt.show()

def plot_monthly_spending(monthly_df):
    monthly_df.plot(kind='line', marker='o', figsize=(10, 6), title='Monthly Spending Over Time')
    plt.xlabel('Month')
    plt.ylabel('Total Amount')
    plt.tight_layout()
    filepath = os.path.join(CHART_DIR, "monthly_spending.png")
    plt.savefig(filepath)
    plt.show()