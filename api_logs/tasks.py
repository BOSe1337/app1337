from app1337.celery import app
from .models import StateUser


@app.task
def clear_users():
    StateUser.objects.all().delete()