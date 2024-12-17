from src.data_collection import fetch_stock_data, fetch_event_data
from src.sentiment_analysis import analyze_sentiment
from src.trading_strategy import generate_signals
from src.backtesting import backtest_strategy
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def main():
    # 1. Collect data
    stock_data = fetch_stock_data("AAPL")
    event_data = fetch_event_data("AAPL")
    print(stock_data.head())
    for article in event_data['articles'][:5]:
        print(article['title'], "-", article['publishedAt'])
    
    # 2. Perform sentiment analysis
    sentiment_scores = analyze_sentiment(event_data)
    analyzer = SentimentIntensityAnalyzer()
    sample_text = "Apple reports record-breaking earnings this quarter!"
    sentiment = analyzer.polarity_scores(sample_text)
    print(sentiment)

    # 3. Generate trading signals
    signals = generate_signals(stock_data, sentiment_scores)
    print("Signals: ", signals)

    # 4. Backtest the strategy
    results = backtest_strategy(stock_data, signals)

    print("Backtesting Results:", results)

if __name__ == "__main__":
    main()
