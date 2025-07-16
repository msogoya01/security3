from flask import Flask, render_template, request, redirect, url_for
import os
import csv
import datetime
from app.dashboard import dashboard_bp
from app.ingestion import load_messages
from app.ml_model import load_model, predict_message
from app.alerting import log_alert, get_alerts

app = Flask(__name__)
app.register_blueprint(dashboard_bp)

# Load ML model and vectorizer at startup
model, vectorizer = load_model()

@app.route('/process', methods=['POST'])
def process_message():
    sender = request.form.get('sender', 'unknown')
    message = request.form.get('message', '')
    message_id = str(int(datetime.datetime.now().timestamp()))
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Append to CSV
    csv_path = os.path.join(os.path.dirname(__file__), '../data/sample_messages.csv')
    with open(csv_path, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([message_id, sender, message, timestamp])

    # Run phishing detection
    pred, prob = predict_message(model, vectorizer, message)
    if pred == 1:  # 1 = phishing
        log_alert(message_id, sender, message, prob)
    return redirect(url_for('dashboard.dashboard'))

@app.route('/health')
def health():
    return {'status': 'ok'}

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)