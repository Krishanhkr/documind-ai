from transformers import pipeline

# Load model globally for efficiency
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_summary(text):
    """Generates a concise summary of the input text using BART model."""
    if not text:
        return "No content found in document."
    if len(text) < 300:
        return text

    chunks = [text[i:i + 1000] for i in range(0, len(text), 1000)]
    summaries = []
    for chunk in chunks:
        result = summarizer(chunk, max_length=150, min_length=50, do_sample=False)
        summaries.append(result[0]['summary_text'])
    return " ".join(summaries)
