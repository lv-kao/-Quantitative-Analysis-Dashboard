import yfinance as yf
import pandas as pd
import numpy as np

def get_price_data(tickers, start, end):
    df = yf.download(tickers, start=start, end=end, auto_adjust=True)["Close"]
    return df

def calculate_technical_indicators(df):
    ma20 = df.rolling(window=20).mean()
    ma50 = df.rolling(window=50).mean()
    daily_returns = df.pct_change().dropna()
    annual_return = daily_returns.mean() * 252
    annual_volatility = daily_returns.std() * np.sqrt(252)
    risk_free = 0.02
    sharpe_ratio = (annual_return - risk_free) / annual_volatility
    return ma20, ma50, daily_returns, annual_return, annual_volatility, sharpe_ratio
