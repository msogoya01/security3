import spacy
import en_core_web_sm
import string

nlp = en_core_web_sm.load()

# Use spaCy's built-in stopwords
stop_words = nlp.Defaults.stop_words

def preprocess_text(text):
    # Lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Tokenize with spaCy
    tokens = [token.text for token in nlp(text)]
    # Remove stopwords
    filtered_tokens = [w for w in tokens if w not in stop_words and w.strip() != '']
    return ' '.join(filtered_tokens) 