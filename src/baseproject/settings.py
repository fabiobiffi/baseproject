"""
Django settings for Base Project project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

# pylint: skip-file

import ast
from pathlib import Path
import os
from concurrent_log_handler import ConcurrentRotatingFileHandler


# Base project version
VERSION = "0.0.0"

# production website url
WEBSITE_URL = ""

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
PRJ_DIR = BASE_DIR.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = ast.literal_eval(os.environ.get("DEBUG", False))

ALLOWED_HOSTS = ["*"]

LOGIN_REDIRECT_URL = "/"

# Application definition

INSTALLED_APPS = [
    # custom application
    "baseproject.apps.frontend",

    # default django application + pip packages
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
    "rest_framework",
    "ckeditor",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.locale.LocaleMiddleware",
]

ROOT_URLCONF = "baseproject.urls"

INTERNAL_IPS = [
    "127.0.0.1",
    "localhost",
    "172.20.0.1",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "baseproject.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DEV_DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'baseproject',
    }
}
PROD_DATABASES = os.environ.get("DATABASES", {
    "default": {
        "ENGINE": os.environ.get("DATABASE_ENGINE"),
        "NAME":  os.environ.get("MYSQL_DATABASE"),
        "USER": os.environ.get("MYSQL_USER"),
        "PASSWORD": os.environ.get("MYSQL_PASSWORD"),
        # the name of the container if we are using docker
        "HOST": os.environ.get("DATABASE_HOST"),
        "PORT": os.environ.get("DATABASE_PORT"),

        'OPTIONS': {
            'charset': 'utf8mb4',
            'use_unicode': True,
        },
    }
})

DATABASES = PROD_DATABASES

# Logging management
LOG_DIR = os.path.join(PRJ_DIR, 'logs')
INFO_LOG_FILE = os.path.join(LOG_DIR, 'info.log')
WARNING_LOG_FILE = os.path.join(LOG_DIR, 'warning.log')
ERROR_LOG_FILE = os.path.join(LOG_DIR, 'error.log')

# Crea la directory dei log se non esiste
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    "formatters": {
        "verbose": {
            "format": "[{levelname}] [{asctime}] [{filename} {lineno}]: {message}",
            "style": "{",
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            "formatter": "verbose",
        },
        'info_file': {
            'level': 'INFO',
            'class': 'concurrent_log_handler.ConcurrentRotatingFileHandler',
            'filename': INFO_LOG_FILE,
            'maxBytes': 10485760,  # 10MB
            'backupCount': 7,
            "formatter": "verbose",
        },
        'warning_file': {
            'level': 'WARNING',
            'class': 'concurrent_log_handler.ConcurrentRotatingFileHandler',
            'filename': WARNING_LOG_FILE,
            'maxBytes': 10485760,  # 10MB
            'backupCount': 7,
            "formatter": "verbose",
        },
        'error_file': {
            'level': 'ERROR',
            'class': 'concurrent_log_handler.ConcurrentRotatingFileHandler',
            'filename': ERROR_LOG_FILE,
            'maxBytes': 10485760,  # 10MB
            'backupCount': 7,
            "formatter": "verbose",
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django': {
            'handlers': ['info_file', 'warning_file', 'error_file'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}

# Password validation + user model
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [] if DEBUG else [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# email settings (please define them in env_settings.py file)
EMAIL_BACKEND = os.environ.get("EMAIL_BACKEND", "")
EMAIL_HOST = os.environ.get("EMAIL_HOST", "")
EMAIL_USE_TLS = os.environ.get("EMAIL_USE_TLS", True)
EMAIL_PORT = os.environ.get("EMAIL_PORT", 587)
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD", "")

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_ROOT = os.path.join(PRJ_DIR, "static")
STATIC_URL = "/static/"

# Media
# https://docs.djangoproject.com/en/4.0/ref/settings/#std:setting-MEDIA_ROOT
# https://docs.djangoproject.com/en/4.0/ref/settings/#std:setting-MEDIA_URL
MEDIA_ROOT = os.path.join(PRJ_DIR, "uploaded")
MEDIA_URL = "/uploaded/"

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ]
}

# for timezone support
USE_TZ = True

# for lot of element in get requestes
DATA_UPLOAD_MAX_NUMBER_FIELDS = 10240

# for the rich text editor, in admin page of sporting center
CKEDITOR_CONFIGS = {
    "default": {
        "width": "auto",
        "height": 300,
        "toolbar": "Custom",
        "toolbar_Custom": [
            ["Styles", "Format"],
            ["Bold", "Italic", "Underline"],
            [
                "BulletedList",
                "NumberedList",
                "-",
                "Outdent",
                "Indent",
                "-",
                "JustifyLeft",
                "JustifyCenter",
                "JustifyRight",
                "JustifyBlock",
            ],
            ["TextColor", "BGColor", "Smiley"],
            ["Image", "Table"],
            ["Link", "Unlink"],
            ["RemoveFormat", "Source"],
        ],
    }
}


# Jazzmin settings
# https://django-jazzmin.readthedocs.io/configuration/
JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "Baseproject Admin",

    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "Base Project",

    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "Base Project",

    # Welcome text on the login screen
    "welcome_sign": "Welcome to Base Project",

    # Copyright on the footer
    "copyright": "Fabio Biffi",

    ############
    # Top Menu #
    ############

    # Links to put along the top menu
    "topmenu_links": [
        {"name": "Frontend Homepage",  "url": "/"},
    ],

    #############
    # User Menu #
    #############

    # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    "usermenu_links": [
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.user"}
    ],

}