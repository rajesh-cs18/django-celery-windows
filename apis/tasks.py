from celery import shared_task
from datetime import datetime

@shared_task
def my_task():
    try:
        now = datetime.now()
        print(f"My Celery task ran at {now}")
        # Your task logic here
    except Exception as e:
        print(f"An error occurred: {e}")
