from flask import Blueprint, render_template
from app.ingestion import load_messages
from app.alerting import get_alerts

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/')
def dashboard():
    messages = load_messages()
    alerts = get_alerts()
    return render_template('dashboard.html', messages=messages.iterrows(), alerts=alerts) 