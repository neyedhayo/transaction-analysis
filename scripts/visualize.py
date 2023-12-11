import gradio as gr
import numpy as np
import pandas as pd
import seaborn as sns
sns.set_style('darkgrid')
import matplotlib.pyplot as plt

def visualize(files):
    # Read data from each file using pandas
    dataframes = []
    for f in files:
        data = pd.read_csv(f)

        # Data cleaning steps
        transaction_data = data[['account_id', 'amount', 'status', 'created_at']]
        transaction_data['created_at'] = pd.to_datetime(transaction_data['created_at'], format = '%d/%m/%Y %H:%M')
        transaction_data = transaction_data.rename(columns={'account_id': 'AccountID', 'amount': 'TransactionAmount', 'status': 'Status', 'created_at': 'DatePeriod'}) #.rename_axis('DateTime')
        transaction_data.set_index('created_at', inplace=True)

        dataframes.append(transaction_data)

    # Generate visualizations
    



demo = gr.Interface(fn=greeting, inputs='text', outputs='text')

if __name__ == "__main__":
    demo.launch(show_api=False)