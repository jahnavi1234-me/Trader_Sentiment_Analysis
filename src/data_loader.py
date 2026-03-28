import pandas as pd

def load_trader_data(path):
    df = pd.read_csv(path)
    df.columns = df.columns.str.strip().str.lower()
    return df


def load_sentiment_data(path):
    df = pd.read_csv(path)

    # Clean columns
    df.columns = df.columns.str.strip().str.lower()
    print("📊 Sentiment Columns:", df.columns)

    # Convert date properly
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date']).dt.date
        df['date'] = pd.to_datetime(df['date'])
    else:
        raise ValueError("❌ 'date' column missing in sentiment data")

    return df