from celery import Celery
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

celery = Celery(app.name, broker=app.config['CACHE_REDIS_URL'])
celery.conf.update(app.config)

@celery.task
def send_daily_reminder():
    # Logic for sending daily reminders (e.g., to service professionals)
    print("Sending daily reminders to service professionals...")

@celery.task
def generate_monthly_report():
    # Logic to generate and email a monthly report
    print("Generating monthly report...")

@celery.task
def export_service_requests_to_csv():
    # Logic to export service requests as CSV
    print("Exporting service requests to CSV...")
