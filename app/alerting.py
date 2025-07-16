import datetime

alerts = []

def log_alert(message_id, sender, message, prob):
    alert = {
        'id': message_id,
        'sender': sender,
        'message': message,
        'probability': prob,
        'timestamp': datetime.datetime.now().isoformat()
    }
    alerts.append(alert)
    return alert

def get_alerts():
    return alerts 