from transformers import pipeline

def generate_summary(text):
    try:
        summarizer = pipeline("summarization", model="facebook/bart-large-cnn", framework="pt", device=-1)
    except Exception:
        return "AI summarizer not available on this deployment. Please run locally for full features."

    if not text or len(text) < 300:
        return text or "No content found."
    parts = [text[i:i + 1000] for i in range(0, len(text), 1000)]
    summary = []
    for p in parts:
        out = summarizer(p, max_length=150, min_length=50, do_sample=False)
        summary.append(out[0]['summary_text'])
    return " ".join(summary)
