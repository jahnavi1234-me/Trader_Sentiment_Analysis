import matplotlib.pyplot as plt
import seaborn as sns

def plot_pnl_boxplot(df, save_path):
    df = df.dropna(subset=['classification'])

    if df.empty:
        print(" No data available for plotting")
        return

    plt.figure(figsize=(8,5))
    sns.boxplot(x='classification', y='closed pnl', data=df)
    plt.title('PnL by Market Sentiment')
    plt.savefig(save_path)
    plt.show()


def plot_avg_pnl_over_time(df, save_path):
    df = df.dropna(subset=['classification'])

    if df.empty:
        print(" No data available for plotting")
        return

    daily = df.groupby('date')['closed pnl'].mean().reset_index()

    plt.figure(figsize=(10,5))
    plt.plot(daily['date'], daily['closed pnl'])
    plt.title('Average Daily PnL')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(save_path)
    plt.show()