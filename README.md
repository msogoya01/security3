# NEC AI-Driven Phishing and SMS Threat Detection System

This project is an AI-powered platform to detect and mitigate phishing and malicious SMS/email threats targeting the National Electoral Commission (NEC) of Tanzania. It leverages NLP and machine learning to classify messages and provides a dashboard for real-time monitoring and response.

## Features
- Ingests SMS/email data (CSV or API)
- Preprocesses and analyzes message content
- AI/ML-based phishing detection
- Real-time alerting and dashboard
- Easily extensible and deployable (Docker, GitHub)

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd nec-phishing-detection
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Download NLTK data:
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   ```
4. (Optional) Download spaCy model:
   ```bash
   python -m spacy download en_core_web_sm
   ```
5. Run the Flask app:
   ```bash
   python -m app.main
   ```

## Usage
- Access the dashboard at `http://localhost:5000` to view messages and flagged threats.
- Add new messages to `data/sample_messages.csv` for testing.

## Project Structure
- `app/` - Source code (Flask app, ML model, preprocessing, dashboard)
- `data/` - Sample data
- `model/` - Trained ML model

## License
MIT 