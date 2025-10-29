# utils/ai_summary.py
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
import nltk

# Ensure punkt downloaded
try:
    nltk.data.find("tokenizers/punkt")
except Exception:
    nltk.download("punkt")

def generate_summary(text, sentences_count=5):
    """Lightweight summarizer using LexRank (sumy). Works well for Render."""
    if not text:
        return "No content found in document."
    # cap text length for performance; if huge, trim to first N chars
    if len(text) > 200000:
        text = text[:200000]

    try:
        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        summarizer = LexRankSummarizer()
        summary_sentences = summarizer(parser.document, sentences_count)
        summary = " ".join(str(s) for s in summary_sentences)
        return summary if summary.strip() else (text[:1000] + "...")
    except Exception as e:
        # fallback: return leading text if summarizer fails
        return text[:1200] + ("..." if len(text) > 1200 else "")
