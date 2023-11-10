from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'basicSetup.settings')

app = Celery('basicSetup')


app.conf.timezone = 'Asia/Karachi'
app.conf.accept_content = ['json']
app.conf.result_serializer = 'json'
app.conf.task_serializer = 'json' 
app.conf.result_backend = 'django-db' 
app.conf.broker_connection_retry_on_startup = True 

app.config_from_object(settings, namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")