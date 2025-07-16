# Part 2: Development of an AI-Driven Cybersecurity Solution

## Title
**AI-Driven Phishing and SMS Threat Detection System for the National Electoral Commission (NEC) of Tanzania**

---

## 1. System Overview
This system is designed to help the National Electoral Commission (NEC) of Tanzania protect the integrity of the electoral process by detecting and flagging phishing or malicious SMS/email messages. The system leverages modern machine learning (ML) and natural language processing (NLP) techniques to classify messages as either legitimate or phishing. It provides a real-time dashboard for monitoring, alerting, and managing potential threats.

**Key Features:**
- **Message Ingestion:** Allows NEC staff to submit SMS/email messages via a web dashboard for analysis. The system can be extended to ingest messages from live SMS/email APIs in the future.
- **Preprocessing:** Utilizes spaCy for advanced text preprocessing, including tokenization (splitting text into words), lowercasing, punctuation removal, and stopword removal. This ensures that the model focuses on the most relevant parts of each message.
- **AI/ML-Based Detection:** Uses a logistic regression model trained on a real, election-related dataset to classify messages. The model is designed to recognize both generic and election-specific phishing tactics.
- **Real-Time Alerting:** If a message is flagged as phishing, it is immediately displayed in a dedicated alert table on the dashboard, allowing for rapid response.
- **Dashboard:** Provides a user-friendly interface for submitting messages, viewing all messages, and monitoring flagged phishing alerts. The dashboard is styled to match NEC branding and is accessible via a web browser.
- **Extensibility:** The system is modular and can be extended with more advanced models, additional data sources, or integration with NEC’s IT infrastructure.

---

## 2. Model Training Process

### **Dataset**
- The model is trained on `election_sms_dataset.csv`, which contains over 80 real and simulated SMS/email messages related to the election process.
- Each message is labeled as either `legitimate` (safe) or `phishing` (malicious).
- The dataset includes a variety of phishing tactics, such as fake links, requests for sensitive information, and urgent calls to action, as well as legitimate election communications.

### **Preprocessing**
- **Lowercasing:** Converts all text to lowercase to ensure uniformity (e.g., "Vote" and "vote" are treated the same).
- **Punctuation Removal:** Strips out punctuation to focus on the core words.
- **Tokenization:** Uses spaCy to split messages into individual words (tokens), which helps the model understand the structure and content of each message.
- **Stopword Removal:** Removes common words (e.g., "the", "and", "is") that do not contribute to phishing detection, using spaCy’s built-in stopword list.

### **Vectorization**
- **TF-IDF Vectorizer:** Converts the preprocessed text into numerical features using Term Frequency-Inverse Document Frequency (TF-IDF). This technique highlights words that are important in a message but not common across all messages, helping the model focus on suspicious terms.

### **Model**
- **Logistic Regression:** A simple yet effective machine learning algorithm for binary classification (phishing vs. legitimate). It is fast, interpretable, and works well with TF-IDF features.
- **Training Script:** The script `train_election_model.py` automates the entire process: loading data, preprocessing, vectorizing, training, and saving the model.

### **Model Files**
- `model/phishing_model.pkl`: The trained logistic regression model.
- `model/tfidf_vectorizer.pkl`: The TF-IDF vectorizer used to transform messages for the model.

### **Retraining the Model**
- To improve the model, simply add more labeled messages to `election_sms_dataset.csv` (e.g., new phishing scams or legitimate election updates).
- Run `python train_election_model.py` to retrain and update the model files. The app will automatically use the new model.

---

## 3. How to Run and Use the App

### **A. Setup**
1. **Install Dependencies:**
   - All required Python packages are listed in `requirements.txt` (Flask, scikit-learn, spaCy, etc.).
   - Install them with:
     ```bash
     pip install -r requirements.txt
     python -m spacy download en_core_web_sm
     ```
2. **Ensure Required Files Exist:**
   - `model/phishing_model.pkl` and `model/tfidf_vectorizer.pkl` (created by the training script)
   - `data/sample_messages.csv` (can be empty except for the header: `id,sender,message,timestamp`)
   - `election_sms_dataset.csv` (for retraining)

### **B. Start the App**
- Run the Flask app with:
  ```bash
  python -m app.main
  ```
- The app will start a local web server (by default at [http://localhost:5000](http://localhost:5000)).

### **C. Use the Dashboard**
- **Submit a Message:** Enter the sender and message content in the form and click "Check Message". The message will be analyzed and added to the CSV.
- **View All Messages:** All submitted messages (including those from the CSV) are displayed in the "All Messages (from CSV)" table.
- **View Flagged Phishing Alerts:** If a message is classified as phishing, it will also appear in the "Flagged Phishing Alerts" table, along with its probability score and timestamp.
- **Retrain the Model:** To improve detection, add new labeled messages to `election_sms_dataset.csv` and rerun the training script.

### **D. Example Workflow**
1. A staff member receives a suspicious SMS about voter registration.
2. They submit the message via the dashboard.
3. The system analyzes the message and, if it is phishing, immediately flags it in the alerts table.
4. The message is also stored in the CSV for record-keeping and future analysis.

---

## 4. Security and Privacy Considerations
- **Local Processing:** All message analysis is performed locally; no sensitive data is sent to external servers or third parties.
- **Data Minimization:** Only the necessary information (sender, message, timestamp) is stored. No personal voter data is required.
- **Access Control:** The dashboard can be restricted to authorized NEC staff by adding authentication (Flask-Login or similar).
- **On-Premises Deployment:** The system can be deployed on NEC’s internal servers for maximum data control and compliance with Tanzanian data protection laws.
- **Auditability:** All flagged phishing messages are logged and can be reviewed for compliance and incident response.
- **Model Updates:** The model can be retrained as new phishing tactics emerge, ensuring ongoing protection.

---

## 5. Deployment and Integration
- **Local or Server Deployment:** The app can be run on a local machine for testing or deployed to a secure server (on-premises or cloud) for production use.
- **Production Considerations:**
  - Use a WSGI server like Gunicorn for better performance and reliability.
  - Enable HTTPS for secure communication.
  - Regularly back up the CSV and model files.
- **Integration:**
  - The system can be integrated with NEC’s SMS/email gateways for automated message ingestion.
  - Alerts can be connected to NEC’s incident response workflow or IT ticketing systems.
- **Extensibility:**
  - The modular design allows for easy integration of more advanced AI models, additional languages (e.g., Swahili), or new data sources (e.g., WhatsApp, social media).

---

## 6. User Guide

### **Submitting a Message**
- Go to the dashboard at [http://localhost:5000](http://localhost:5000).
- Enter the sender and message content in the form.
- Click "Check Message" to submit.

### **Viewing Results**
- **All Messages Table:** Shows every message submitted, with sender, content, and timestamp.
- **Flagged Phishing Alerts Table:** Shows only those messages detected as phishing, with probability/confidence score and timestamp.

### **Retraining the Model**
- Add new labeled messages to `election_sms_dataset.csv`.
- Run `python train_election_model.py` to update the model.
- Restart the Flask app to use the new model.

### **Best Practices**
- Regularly update the dataset with new phishing examples.
- Review flagged alerts to ensure accuracy and improve the model.
- Restrict dashboard access to authorized personnel.

---

## 7. Screenshots (Optional)
- Add screenshots of the dashboard, message submission form, and alert tables to your submission for clarity and demonstration.
- Example: ![Dashboard Screenshot](dashboard_screenshot.png)

---

## 8. Contact and Support
- For technical support, contact the project maintainer or refer to the README.md for setup and troubleshooting.
- For further development, consult the codebase and consider extending the system with new features as needed by NEC. 

---

Perfect! Here’s how to push your project to your GitHub repository at  
**[https://github.com/msogoya01/security3.git](https://github.com/msogoya01/security3.git)**

---

## **Step-by-Step Instructions**

1. **Initialize Git (if you haven’t already):**
   ```bash
   git init
   ```

2. **Add all your files:**
   ```bash
   git add .
   ```

3. **Commit your changes:**
   ```bash
   git commit -m "Initial commit: NEC AI-Driven Phishing Detection System"
   ```

4. **Add your GitHub remote:**
   ```bash
   git remote add origin https://github.com/msogoya01/security3.git
   ```

5. **Set the main branch (if not already set):**
   ```bash
   git branch -M main
   ```

6. **Push your code to GitHub:**
   ```bash
   git push -u origin main
   ```

---

## **After Pushing**

- Your code and documentation will be available at:  
  [https://github.com/msogoya01/security3](https://github.com/msogoya01/security3)

- You can share this link with anyone who needs to access your project.

---

## **Next Steps (Optional)**
- If you want to deploy your Flask app online (for a live demo), let me know and I’ll guide you through deploying to a platform like Render, Railway, or PythonAnywhere.

---

If you encounter any errors during the push, paste the error message here and I’ll help you resolve it! 