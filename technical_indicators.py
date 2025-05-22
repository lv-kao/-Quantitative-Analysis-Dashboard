import pandas as pd

def moving_average(series: pd.Series, window: int) -> pd.Series:
    """
    計算簡單移動平均線 (Simple Moving Average, SMA)
    """
    return series.rolling(window=window).mean()

def exponential_moving_average(series: pd.Series, window: int) -> pd.Series:
    """
    計算指數移動平均線 (Exponential Moving Average, EMA)
    """
    return series.ewm(span=window, adjust=False).mean()

def rsi(series: pd.Series, window: int = 14) -> pd.Series:
    """
    計算相對強弱指標 (Relative Strength Index, RSI)
    """
    delta = series.diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(window=window).mean()
    avg_loss = loss.rolling(window=window).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def macd(series: pd.Series, fast_period: int = 12, slow_period: int = 26, signal_period: int = 9):
    """
    計算移動平均收斂擴散指標 (MACD) 和訊號線
    """
    ema_fast = exponential_moving_average(series, fast_period)
    ema_slow = exponential_moving_average(series, slow_period)
    macd_line = ema_fast - ema_slow
    signal_line = macd_line.ewm(span=signal_period, adjust=False).mean()
    histogram = macd_line - signal_line
    return macd_line, signal_line, histogram
