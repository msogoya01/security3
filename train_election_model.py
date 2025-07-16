import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
import spacy
import string

# Load your labeled data
df = pd.read_csv('election_sms_dataset.csv')

# Map labels to 0/1
df['Label'] = df['Label'].map({'legitimate': 0, 'phishing': 1})

# Preprocess using spaCy (same as your app)
nlp = spacy.load("en_core_web_sm")
stop_words = nlp.Defaults.stop_words

def preprocess_text(text):
    text = str(text).lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = [token.text for token in nlp(text)]
    filtered_tokens = [w for w in tokens if w not in stop_words and w.strip() != '']
    return ' '.join(filtered_tokens)

df['processed'] = df['Message'].apply(preprocess_text)

# Vectorize
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['processed'])
y = df['Label']

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X, y)

# Save model and vectorizer
joblib.dump(model, 'model/phishing_model.pkl')
joblib.dump(vectorizer, 'model/tfidf_vectorizer.pkl')
print('Model and vectorizer saved to model/') 