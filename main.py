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
    analyzer = SentimentIntensityAnalyzer()
    sentiment_scores = []

    for article in event_data['articles'][:5]:
        # Extract the title and description (or any other content you want to analyze)
        article_title = article.get('title', '')
        article_description = article.get('description', '')
    
        # Combine title and description to form the full text to analyze
        full_text = f"{article_title} {article_description}"

        # Perform sentiment analysis
        sentiment = analyzer.polarity_scores(full_text)

        sentiment_scores.append(sentiment['compound'])
    
        # Print the sentiment result for each article
        print(f"Title: {article_title}")
        print(f"Published At: {article['publishedAt']}")
        print(f"Sentiment: {sentiment}")
        print("-" * 50)  # Separator for readability

    print(sentiment_scores)
    # generate trading signals
    signals = generate_signals(stock_data, sentiment_scores)

    # backtest the strategy
    results = backtest_strategy(stock_data, signals, ticker)

    print("Backtesting Results:", results)

if __name__ == "__main__":
    main()
