"""
Django settings for crossfit project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os

from pathlib import Path

from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.

# print(Path(__file__).resolve().parent)
# Following settings are imported from .env:
#     DB Settings:
#         DJANGO_SECRET_KEY
#         DJANGO_DB_USER_PASS
#         DJANGO_DB_ENGINE
#         DJANGO_DB_NAME
#         DJANGO_DB_USER
#         DJANGO_DB_HOST
#         DJANGO_DB_PORT
#     Email settings:
#         EMAIL_HOST
#         EMAIL_HOST_PASSWORD
#         EMAIL_HOST_USER
#         EMAIL_PORT
#         EMAIL_USE_SSL
#         DEFAULT_FROM_EMAIL



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


AUTHENTICATION_BACKENDS = [
    
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #For allauth
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    #Crossfit apps
    'rest_framework',
    'crispy_forms',
    'frontend',
    'api',
    'db',
]

SITE_ID = 1


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'crossfit.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "frontend/templates/allauth" ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                 # `allauth` needs this from django
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'crossfit.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': os.getenv("DJANGO_DB_ENGINE"),
        'NAME': os.getenv("DJANGO_DB_NAME"),
        'USER': os.getenv("DJANGO_DB_USER"),
        'PASSWORD': os.getenv("DJANGO_DB_USER_PASS"),
        'HOST': os.getenv("DJANGO_DB_HOST"),
        'PORT': os.getenv("DJANGO_DB_PORT"), #Default is 5432
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    #Password rules removed
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]

AUTH_USER_MODEL = 'db.User'


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'EET'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/frontend/static/'
STATICFILES_DIRS = [
    os.path.join( BASE_DIR, 'frontend/static/')
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'


# create root dir for all images
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SESSION_COOKIE_AGE = 60*10 #in seconds
SESSION_SAVE_EVERY_REQUEST = True

CSRF_USE_SESSIONS = True


#EMAIL settings
# TODO: check gmail smtp: https://kinsta.com/blog/gmail-smtp-server/
# TODO: check email works with settings in .env

EMAIL_HOST= os.getenv("EMAIL_HOST")
EMAIL_HOST_PASSWORD	= os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_HOST_USER	= os.getenv('EMAIL_HOST_USER')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_USE_SSL = os.getenv('EMAIL_USE_SSL')
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')

#Allauth settings
ACCOUNT_FORMS = {
    'signup' : 'frontend.forms.CreateUserForm',
}

LOGIN_REDIRECT_URL = 'index'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
