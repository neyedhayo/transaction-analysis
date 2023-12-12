import numpy as np
import pandas as pd
import seaborn as sns
sns.set_style('darkgrid')
import matplotlib.pyplot as plt
import io


# VISUALIZATION 1 -----
def visualize_users_exceeding_50(df):
    # exploratory data preparation
    monthly_count = df.groupby([df.index.month, 'AccountID'])['TransactionAmount'].count() # for each AccountID per month, count their total amount of transactionamount
    exceeded_50per_month = monthly_count[monthly_count > 50] # filter accountID with transactions higher than 50
    exceeded_50per_month_df = pd.DataFrame(exceeded_50per_month.reset_index(name='TransactionCount')) # store in a dataframe and reset/rename the count by the index
    exceeded_50per_month_df.rename(columns={'DatePeriod': 'Month'}, inplace=True)

    # Map month numbers to names
    month_mapping = {
        1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
        7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'
    }

    # compute the month integer to their precise months by mapping
    exceeded_50per_month_df['Month'] = exceeded_50per_month_df['Month'].map(month_mapping)
    # Group by month to get total number of users exceeding 50 transactions
    total_users_exceeding_50 = exceeded_50per_month_df.groupby('Month')['AccountID'].count().reindex(month_mapping.values())

    # Bar plot for TransactionCount by Month
    plt.figure(figsize=(12, 6))
    ax = sns.barplot(x=total_users_exceeding_50.index, y=total_users_exceeding_50.values, palette='viridis')
    plt.title('Total Number of Users Exceeding 50 Monthly Transactions')
    plt.xlabel('Month')
    plt.ylabel('Number of Users')

    # Adding the count above the bars
    for p in ax.patches:
        ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', fontsize=10, color='black', xytext=(0, 5),
                    textcoords='offset points')
    plt.show()

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close() # Close the plot to free resources
    return buf


# VISUALIZATION 2 ---
def visualize_highest_monthly_transaction_user(df):
    # exploratory data visualization
    highest_transaction_per_month_idx = df.groupby([df.index.month])['TransactionAmount'].idxmax()
    highest_transactions = df.loc[highest_transaction_per_month_idx]

    highest_transactions['Month'] = highest_transactions.index.month.map(month_mapping)
    # Remove duplicate months if any (though unlikely in this scenario)
    highest_transactions = highest_transactions.drop_duplicates(subset=['Month'])

    # Function to format the amounts
    def format_amount(value):
        if value >= 1e6:
            return f'{value / 1e6:.1f}M'
        elif value >= 1e3:
            return f'{value / 1e3:.1f}K'
        else:
            return str(value)

    # Bar plot for the highest transaction amount by month
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(x='Month', y='TransactionAmount', data=highest_transactions, palette='viridis', order=month_mapping.values())
    ax.ticklabel_format(style='plain', axis='y')  # Disable scientific notation on the y-axis
    plt.title('Highest Transaction Amount by Unique User for Each Month')
    plt.xlabel('Month')
    plt.ylabel('Transaction Amount')

    # Adding formatted amounts above the bars
    for p in ax.patches:
        formatted_amount = format_amount(p.get_height())
        ax.annotate(formatted_amount, (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', fontsize=10, color='black', xytext=(0, 5),
                    textcoords='offset points')
    plt.show()

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close() # Close the plot to free resources
    return buf