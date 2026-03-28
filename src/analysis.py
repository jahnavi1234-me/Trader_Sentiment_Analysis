def calculate_pnl_by_sentiment(df):
    df = df.dropna(subset=['classification'])
    return df.groupby('classification')['closed pnl'].agg(['mean', 'median', 'sum'])


def win_rate_by_sentiment(df):
    df = df.dropna(subset=['classification'])
    df['win'] = df['closed pnl'] > 0
    return df.groupby('classification')['win'].mean() * 100


def trader_performance_by_account(df):
    return df.groupby('account')['closed pnl'].sum().sort_values(ascending=False)