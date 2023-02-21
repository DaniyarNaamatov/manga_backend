from .env_reader import env, csv
from datetime import timedelta
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# SECRET_KEY
SECRET_KEY = env("SECRET_KEY")

# ALLOWED_HOSTS
ALLOWED_HOSTS = env("ALLOWED_HOSTS", cast=csv())

# DEBUG
DEBUG = env("DEBUG", default=False, cast=bool)

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=7),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=30),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": False,
    }