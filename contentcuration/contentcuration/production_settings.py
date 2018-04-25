import os
from .settings import *

MEDIA_ROOT = STORAGE_ROOT

SITE_ID = int(os.getenv("SITE_ID") or "1")

SESSION_ENGINE = "django.contrib.sessions.backends.db"

# email settings
EMAIL_BACKEND = 'postmark.django_backend.EmailBackend'
POSTMARK_API_KEY = os.getenv("EMAIL_CREDENTIALS_POSTMARK_API_KEY")

LANGUAGE_CODE = os.getenv("LANGUAGE_CODE") or "en"
