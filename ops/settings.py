"""
Django settings for ops project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3$%*&qqr2)ct_d2fq8=hny*-y^yvip(mhs4n1m#)$wjfy#znp)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'idcs.apps.IdcsConfig',
    'cabinet.apps.CabinetConfig',
    'users.apps.UsersConfig',
    'manufacturer.apps.ManufacturerConfig',
    'servers.apps.ServersConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ops.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'ops.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'devops',
        'USER': 'ronin',
        'PASSWORD': 'ttiswsy.1006',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'OPTIONS': {
            'init_command': 'SET default_storage_engine=INNODB;'
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        "default": {
            "format": '%(asctime)s %(name)s %(lineno)s %(levelname)s  %(message)s',
            "datefmt": "%Y-%m-%d %H:%M:%S"
        }
    },

    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': '/tmp/debug.log',
            'when': "D",
            'interval': 1,
            'formatter': 'default'
        },
        "request": {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/tmp/request.log',
            'formatter': 'default'
        },
        "server": {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/tmp/server.log',
            'formatter': 'default'
        },
        "root": {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/tmp/root.log',
            'formatter': 'default'
        },

        "db_backends": {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/tmp/db_backends.log',
            'formatter': 'default'
        }
    },
    'loggers': {
        "reboot": {
            "level": "DEBUG",
            "handlers": ["console", "file"],
            'propagate': True,
        },
        "django": {
            "level": "DEBUG",
            "handlers": ["console", "file"],
            'propagate': True,
        },
        "django.request": {
            "level": "DEBUG",
            "handlers": ["request"],
            'propagate': False,
        },
        "django.server": {
            "level": "DEBUG",
            "handlers": ["server"],
            'propagate': False,
        },
        "django.db.backends": {
            "level": "DEBUG",
            "handlers": ["db_backends"],
            'propagate': False,
        }
    },
    'root': {
        "level": "DEBUG",
        "handlers": ["file"],
    }
}

LOGGING = {}
