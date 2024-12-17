from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment(event_data):
    analyzer = SentimentIntensityAnalyzer()
    sentiment_scores = []

    for event in event_data['articles']:
        if event['description'] is not None:
            sentiment = analyzer.polarity_scores(event['description'])
            sentiment_scores.append(sentiment['compound'])
        else:
            sentiment_scores.append(0)

    return sentiment_scores