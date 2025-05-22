from data_fetch import get_price_data, calculate_technical_indicators
from portfolio_opt import optimize_portfolio
from visualize import plot_price_and_ma, plot_sharpe_bar, plot_correlation_heatmap, plot_portfolio_weights

tickers = ["AAPL", "GOOG", "TSLA", "MSFT", "AMZN"]
start_date = "2024-01-01"
end_date = "2025-05-21"

price_df = get_price_data(tickers, start_date, end_date)

ma20, ma50, daily_returns, annual_return, annual_volatility, sharpe_ratio = calculate_technical_indicators(price_df)

for ticker in tickers:
    plot_price_and_ma(price_df, ma20, ma50, ticker)

plot_sharpe_bar(sharpe_ratio)

plot_correlation_heatmap(daily_returns)

weights = optimize_portfolio(daily_returns)

plot_portfolio_weights(weights)
