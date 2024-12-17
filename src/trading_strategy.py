def generate_signals(stock_data, sentiment_scores, threshold=0.5):
    signals = []

    for i, sentiment in enumerate(sentiment_scores):
        if sentiment > threshold:
            signals.append("Buy")
        elif sentiment < -threshold:
            signals.append("Sell")
        else:
            signals.append("Hold")

    return signals
