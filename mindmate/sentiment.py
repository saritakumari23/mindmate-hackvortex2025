from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    mood = "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"
    return {
        'polarity': polarity,
        'mood': mood,
        'summary': f"Your journal entry feels {mood.lower()}."
    }
