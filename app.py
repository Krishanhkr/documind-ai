from flask import Flask, render_template, request, redirect, url_for
from utils.pdf_parser import extract_text_from_pdf
from utils.ai_summary import generate_summary
from utils.text_analysis import analyze_text
import os, uuid

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['SUMMARY_FOLDER'] = 'summaries'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['SUMMARY_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files.get('file')
    if not file:
        return redirect(url_for('index'))
    filename = f"{uuid.uuid4().hex}_{file.filename}"
    path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(path)

    text = extract_text_from_pdf(path)
    summary = generate_summary(text)
    insights = analyze_text(text)

    return render_template('dashboard.html',
                           filename=file.filename,
                           summary=summary,
                           insights=insights)

if __name__ == '__main__':
    app.run(debug=True)
