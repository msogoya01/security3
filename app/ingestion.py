import pandas as pd
import os

def load_messages(csv_path=None):
    if csv_path is None:
        csv_path = os.path.join(os.path.dirname(__file__), '../data/sample_messages.csv')
    if not os.path.exists(csv_path):
        return pd.DataFrame(columns=['id', 'sender', 'message', 'timestamp'])
    return pd.read_csv(csv_path) 