"""
Django settings for CodeTopia project.

Generated by 'django-admin startproject' using Django 3.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=03=#8t9490(*)()(0][=-05qwnb_lum(454j$buh7%'
# try:
#     SECRET_KEY = os.environ.get("SECRET_KEY")
# except KeyError:
#     SECRET_KEY = '=03=#8t9490(*)()(0][=-05qwnb_lum(454j$buh7%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # Project app
    'account.apps.AccountConfig',

    # Third party apps

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'CodeTopia.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ os.path.join(BASE_DIR, "templates") ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'CodeTopia.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

"""Date Related Settings"""
FIRST_DAY_OF_WEEK = 1 # Monday


"""Email Related Settings"""
# For development use filebased EmailBackend
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = os.path.join(BASE_DIR, "email_archive")

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get("EMAIL_ADDRESS")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_PASSWORD")
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_USE_LOCALTIME = True

DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL")
SERVER_EMAIL = os.environ.get("SERVER_EMAIL")


"""Authentication Related Settings"""
LOGIN_URL = "/user/login/"
LOGIN_REDIRECT_URL = "/"

LOGOUT_REDIRECT_URL = "/"

PASSWORD_RESET_TIMEOUT_DAYS = 1


"""Upload Related Settings"""
DATA_UPLOAD_MAX_MEMORY_SIZE = 2621440 # 2.5MB
FILE_UPLOAD_MAX_MEMORY_SIZE = 2621440 # 2.5 MB

FILE_UPLOAD_HANDLERS = [
    'django.core.files.uploadhandler.MemoryFileUploadHandler',
    'django.core.files.uploadhandler.TemporaryFileUploadHandler',
]


"""Static File Related Settings"""
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]