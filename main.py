from src.data_collection import fetch_stock_data, fetch_event_data
from src.sentiment_analysis import analyze_sentiment
from src.trading_strategy import generate_signals
from src.backtesting import backtest_strategy
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def main():
    # input ticker
    ticker = input("Enter the stock ticker: ").strip().upper()
    print(f"Fetching data for {ticker}...")

    # collect data
    stock_data = fetch_stock_data(ticker)
    event_data = fetch_event_data(ticker)
    print(stock_data.head())

    # perform sentiment analysis
    sentiment_scores = analyze_sentiment(event_data)

    # generate trading signals
    signals = generate_signals(stock_data, sentiment_scores)

    # backtest the strategy
    results = backtest_strategy(stock_data, signals, ticker)

    print("Backtesting Results:", results)

if __name__ == "__main__":
    main()
