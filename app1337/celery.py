import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app1337.settings")
app = Celery("app1337")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "clears_users": {
        "task": "api_logs.tasks.clear_users",
        "schedule": crontab(
            minute=0,
            hour=0,
            day_of_month=1,
        ),
    },
}