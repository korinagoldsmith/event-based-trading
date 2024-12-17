import pandas as pd

def backtest_strategy(stock_data, signals, ticker='AAPL', initial_cash=10000):
    # Initialize cash and holdings
    cash = initial_cash
    holdings = 0

    # Handle MultiIndex columns
    if isinstance(stock_data.columns, pd.MultiIndex):
        # Extract data for the specified ticker
        stock_data = stock_data.xs(ticker, level='Ticker', axis=1)
        print(f"Columns after xs(): {stock_data.columns}")

    if 'Close' not in stock_data.columns:
        raise ValueError("The 'Close' column is missing in the stock data.")

    print(stock_data.head())  # Debugging output
    print(stock_data.columns)  # Debugging output

    # Backtesting loop
    for i, signal in enumerate(signals):
        price = stock_data['Close'].iloc[i]
        if signal == "Buy" and cash >= price:
            holdings += 1
            cash -= price
        elif signal == "Sell" and holdings > 0:
            holdings -= 1
            cash += price

    # Final portfolio value
    final_price = stock_data['Close'].iloc[-1]
    portfolio_value = cash + holdings * final_price

    return portfolio_value - initial_cash