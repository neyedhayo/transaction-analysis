import gradio as gr
import pandas as pd
from visualization import visualize_users_exceeding_50, visualize_highest_monthly_transaction_user


def visualize(files):
    # Read data from each file using pandas
    # dataframes = []
    # for f in files:
        # data = pd.read_csv(f)

        # # Data cleaning steps
        # transaction_data = data[['account_id', 'amount', 'status', 'created_at']]
        # transaction_data['created_at'] = pd.to_datetime(transaction_data['created_at'], format = '%d/%m/%Y %H:%M')
        # transaction_data = transaction_data.rename(columns={'account_id': 'AccountID', 'amount': 'TransactionAmount', 'status': 'Status', 'created_at': 'DatePeriod'}) #.rename_axis('DateTime')
        # transaction_data.set_index('created_at', inplace=True)
    data = pd.read_csv(files)

    # Data cleaning steps
    transaction_data = data[['account_id', 'amount', 'status', 'created_at']]
    transaction_data['created_at'] = pd.to_datetime(transaction_data['created_at'], format = '%d/%m/%Y %H:%M')
    transaction_data = transaction_data.rename(columns={'account_id': 'AccountID', 'amount': 'TransactionAmount', 'status': 'Status', 'created_at': 'DatePeriod'}) #.rename_axis('DateTime')
    transaction_data.set_index('created_at', inplace=True)
    # dataframes.append(transaction_data)

    # Function call of visualization
    vis1 = visualize_users_exceeding_50(transaction_data[0])
    vis2 = visualize_highest_monthly_transaction_user(transaction_data[0])

    return vis1, vis2


# Gradio interface
demo = gr.Interface(fn=visualize, inputs='file', outputs=['image', 'image'])

if __name__ == "__main__":
    demo.launch(show_api=False)