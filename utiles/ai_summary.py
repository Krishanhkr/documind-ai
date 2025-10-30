# utils or utiles / ai_summary.py
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
import nltk

# make sure punkt is available
try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")

def generate_summary(text, sentences_count=5):
    """Lightweight pure-Python summarizer using LexRank (Sumy)."""
    if not text:
        return "No content found in document."
    if len(text) > 200000:
        text = text[:200000]
    try:
        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        summarizer = LexRankSummarizer()
        sentences = summarizer(parser.document, sentences_count)
        return " ".join(str(s) for s in sentences) or text[:1200]
    except Exception as e:
        return text[:1200]
