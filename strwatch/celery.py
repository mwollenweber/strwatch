import os
from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Watchman.settings")

app = Celery("strwatch")
app.conf.timezone = "UTC"
app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.update(
    task_serializer="pickle", result_serializer="pickle", accept_content=["pickle"]
)

app.autodiscover_tasks()
