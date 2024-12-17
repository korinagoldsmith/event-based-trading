def generate_signals(stock_data, sentiment_scores, threshold=0.5):
    signals = []

    for sentiment in sentiment_scores:
        if sentiment > threshold:
            signals.append("Buy")
        elif sentiment < -threshold:
            signals.append("Sell")
        else:
            signals.append("Hold")

    return signals
