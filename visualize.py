import matplotlib.pyplot as plt
import seaborn as sns

def plot_price_and_ma(df, ma20, ma50, ticker):
    plt.figure(figsize=(14,7))
    plt.plot(df[ticker], label='Close Price')
    plt.plot(ma20[ticker], label='MA20')
    plt.plot(ma50[ticker], label='MA50')
    plt.title(f'{ticker} 價格與移動平均線')
    plt.legend()
    plt.show()

def plot_sharpe_bar(sharpe):
    sharpe.sort_values(ascending=False).plot(kind='bar', color='green')
    plt.title('各股票夏普率')
    plt.ylabel('Sharpe Ratio')
    plt.show()

def plot_correlation_heatmap(returns):
    corr = returns.corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title('股票報酬率相關係數熱圖')
    plt.show()

def plot_portfolio_weights(weights):
    weights.plot(kind='bar', color='blue')
    plt.title('投資組合權重')
    plt.ylabel('權重')
    plt.show()
