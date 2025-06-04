# app.py
# A simple Flask application to summarize PDF documents
from flask import Flask, render_template, request
from PyPDF2 import PdfReader
from summarizer import summarize_text

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    summary = ""
    if request.method == "POST":
        pdf = request.files["pdf"]
        if pdf:
            reader = PdfReader(pdf)
            text = "".join([page.extract_text() for page in reader.pages if page.extract_text()])
            summary = summarize_text(text)
    return render_template("index.html", summary=summary)

if __name__ == "__main__":
    app.run(debug=True)
