import yfinance as yf
import matplotlib.pyplot as plt
from technical_indicators import moving_average, rsi, macd

def main():
    # 抓取股票歷史價格
    ticker = "AAPL"
    df = yf.download(ticker, start="2023-01-01", end="2024-01-01", auto_adjust=True)

    close = df['Close']

    # 計算技術指標
    ma20 = moving_average(close, 20)
    rsi14 = rsi(close, 14)
    macd_line, signal_line, hist = macd(close)

    # 畫收盤價和20日移動平均線
    plt.figure(figsize=(12,6))
    plt.plot(close, label='Close Price')
    plt.plot(ma20, label='MA20')
    plt.title(f"{ticker} 收盤價與20日移動平均線")
    plt.legend()
    plt.show()

    # 畫RSI 指標
    plt.figure(figsize=(12,3))
    plt.plot(rsi14, label='RSI14', color='orange')
    plt.axhline(70, color='red', linestyle='--')  # 超買
    plt.axhline(30, color='green', linestyle='--')  # 超賣
    plt.title(f"{ticker} RSI 指標")
    plt.legend()
    plt.show()

    # 畫MACD 指標
    plt.figure(figsize=(12,4))
    plt.plot(macd_line, label='MACD Line')
    plt.plot(signal_line, label='Signal Line')
    plt.bar(hist.index, hist, label='Histogram', color='gray')
    plt.title(f"{ticker} MACD 指標")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
