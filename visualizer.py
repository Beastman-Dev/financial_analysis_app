import matplotlib.pyplot as plt

def plot_summary_by_category(summary_df):
    summary_df.plot(kind='bar', figsize=(10, 6), title='Spending by Category')
    plt.xlabel('Category')
    plt.ylabel('Total Amount')
    plt.tight_layout()
    plt.savefig('financial_analysis/spending_by_category.png')
    plt.show()

def plot_monthly_spending(monthly_df):
    monthly_df.plot(kind='line', marker='o', figsize=(10, 6), title='Monthly Spending Over Time')
    plt.xlabel('Month')
    plt.ylabel('Total Amount')
    plt.tight_layout()
    plt.savefig('financial_analysis/monthly_spending.png')
    plt.show()