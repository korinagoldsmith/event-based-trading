from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment(event_data):
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

    return sentiment_scores