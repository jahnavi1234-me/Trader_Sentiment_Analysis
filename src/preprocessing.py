import pandas as pd

def preprocess_trader_data(trader_df):
    trader_df.columns = trader_df.columns.str.strip().str.lower()
    print("Trader Columns:", trader_df.columns)

    # Use timestamp IST (best alignment)
    if 'timestamp ist' in trader_df.columns:
        trader_df['date'] = pd.to_datetime(trader_df['timestamp ist'], dayfirst=True).dt.date
    elif 'timestamp' in trader_df.columns:
        trader_df['date'] = pd.to_datetime(trader_df['timestamp']).dt.date
    else:
        raise ValueError(" No valid timestamp column found")

    trader_df['date'] = pd.to_datetime(trader_df['date'])

    return trader_df


def merge_datasets(trader_df, sentiment_df):
    merged_df = trader_df.merge(sentiment_df, on='date', how='left')
    return merged_df


def save_merged_data(df, path):
    df.to_csv(path, index=False)