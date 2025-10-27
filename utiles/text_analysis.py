from textblob import TextBlob
import re

def analyze_text(text):
    """Analyzes sentiment and extracts top keywords."""
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    words = re.findall(r'\w+', text.lower())
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    keywords = sorted(freq, key=freq.get, reverse=True)[:10]
    return {
        "sentiment": "Positive" if sentiment > 0 else "Negative" if sentiment < 0 else "Neutral",
        "word_count": len(words),
        "keywords": keywords
    }
