from flask import Flask, render_template, request, redirect, url_for
import os
from datetime import datetime

app = Flask(__name__)

DATA_FILE = "feedback.txt"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form.get('name', 'Anonymous').strip()
        message = request.form.get('message', '').strip()
        if not message:
            return redirect(url_for('feedback'))
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(DATA_FILE, 'a', encoding='utf-8') as f:
            f.write(f"{timestamp} | {name}: {message}\n")
        return redirect(url_for('thank_you'))
    return render_template("feedback.html")

@app.route('/thank-you')
def thank_you():
    return render_template("thank_you.html")

@app.route('/view')
def view_feedback():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f.readlines()]
    else:
        lines = []
    return render_template("view.html", feedback=lines)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
