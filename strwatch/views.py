import logging
from datetime import datetime, timedelta, timezone
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import authenticate, logout  # , login
from django.shortcuts import render, redirect
from django.utils.html import escape
from django.utils.timezone import make_aware
from django.template import loader
from django.conf import settings
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
)
from django.contrib.auth import login as auth_login
from django.views.decorators.http import require_http_methods

logger = logging.getLogger(__name__)

def current_datetime(request):
    now = datetime.utcnow()
    return JsonResponse({"status": "ok", "now": f"{now.isoformat()}"})


def status(request):
    return current_datetime(request)
