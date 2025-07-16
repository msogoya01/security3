import joblib
import os
from app.preprocess import preprocess_text

def load_model(model_path=None, vectorizer_path=None):
    if model_path is None:
        model_path = os.path.join(os.path.dirname(__file__), '../model/phishing_model.pkl')
    if vectorizer_path is None:
        vectorizer_path = os.path.join(os.path.dirname(__file__), '../model/tfidf_vectorizer.pkl')
    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)
    return model, vectorizer

def predict_message(model, vectorizer, message):
    processed = preprocess_text(message)
    X = vectorizer.transform([processed])
    pred = model.predict(X)[0]
    prob = model.predict_proba(X)[0].max()
    return pred, prob 