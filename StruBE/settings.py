# -*- coding : utf-8 -*-

##    Copyright (C) 2015 Hungler Arnaud
##
##    This program is free software; you can redistribute it and/or modify
##    it under the terms of the GNU General Public License as published by
##    the Free Software Foundation; either version 2 of the License, or
##    (at your option) any later version.
##
##    This program is distributed in the hope that it will be useful,
##    but WITHOUT ANY WARRANTY; without even the implied warranty of
##    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
##    GNU General Public License for more details.
##
##    You should have received a copy of the GNU General Public License along
##    with this program; if not, write to the Free Software Foundation, Inc.,
##    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import os
import ConfigParser
import random
import logging
from logging.config import dictConfig

import log_dev
import log_prod

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Read config.ini
config = ConfigParser.ConfigParser()
config_file = os.path.join(BASE_DIR, "config.ini")
try:
    with open(config_file): pass
except IOError:
    print "No config file. Please create it, using the provided template."
    raise
config.read(config_file)

# SECRET_KEY
secret_dir = os.path.join(BASE_DIR, "secret")
secret_file = os.path.join(secret_dir, "secret_file.txt")
try:
    SECRET_KEY = open(secret_file).read().strip()
except IOError:
    chars = \
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+'
    SECRET_KEY = ''.join([random.SystemRandom().choice(chars)
        for i in range(50)])
    try:
        os.makedirs(secret_dir)
    except OSError as e:
        if e.errno == errno.EEXIST and os.path.isdir(secret_dir):
            pass
        else:
            raise
    with open(secret_file, 'w') as f:
        f.write(SECRET_KEY)

# Site ID
SITE_ID = 1

# DEBUG from config.ini
DEBUG = eval(config.get('DEFAULT', 'debug'))

# Logging
LOGGING = {}
if DEBUG:
    LOGGING = log_dev.LOGGING
else:
    LOGGING = log_prod.LOGGING

dictConfig(LOGGING)
log = logging.getLogger(__name__)
log.debug("Log configuration loaded")

# DATABASES from config.ini
default_db = {}
engine = config.get("DATABASE", "engine")
if engine == "sqlite3":
    default_db['ENGINE'] = "django.db.backends." + engine
    name = config.get("DATABASE", "path")
    wholename = os.path.join(BASE_DIR, name)
    default_db['NAME'] = wholename
elif engine in ("mysql", "oracle", "postgresql_psycopg2"):
    default_db['ENGINE'] = "django.db.backends." + engine
    default_db['NAME'] = config.get("DATABASE", "name")
    default_db['USER'] = config.get("DATABASE", "user")
    default_db['PASSWORD'] = config.get("DATABASE", "password")
    default_db['HOST'] = config.get("DATABASE", "host")
    default_db['PORT'] = config.get("DATABASE", "port")
else:
    print "Bad database engine"
    raise ValueError

DATABASES = {'default': default_db}
log.debug("Database configured : " + str(DATABASES))

# ALLOWED_HOSTS from config.ini
ALLOWED_HOSTS = eval(config.get('DEFAULT', 'hosts'))
log.debug("Allowed hosts : " + str(ALLOWED_HOSTS))

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'tinymce',
    'account',
    'envelope',
    'myaccount',
    'crispy_forms',
    'StruBE',
    'contaminer',
    'publications',
    'news',
]
log.debug("Applications : " + str(INSTALLED_APPS))

# Load Middlewares
MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'account.middleware.LocaleMiddleware',
    'account.middleware.TimezoneMiddleware',
]
log.debug("Middlewares : " + str(MIDDLEWARE_CLASSES))

# Templates configuration
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

# URLCONF
ROOT_URLCONF = 'StruBE.urls'

# WSGI
WSGI_APPLICATION = 'StruBE.wsgi.application'

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Account configuration
AUTHENTICATION_BACKEND = [
        'account.auth_backends.EmailAuthenticationBackend',
]
ACCOUNT_EMAIL_CONFIRMATION_REQUIRED = True
ACCOUNT_EMAIL_UNIQUE = True
LOGIN_URL = "/account/login"

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
static_path = config.get('PATHS', 'static')
STATIC_ROOT = os.path.join(BASE_DIR, static_path)

STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'StruBE/static'),
        ]

# Media files (Uploaded by users)
MEDIA_URL = '/media/'
media_path = config.get('PATHS', 'media')
MEDIA_ROOT = os.path.join(BASE_DIR, media_path)

# Email
EMAIL_HOST = config.get('EMAIL', 'host')
EMAIL_PORT = eval(config.get('EMAIL', 'port'))
EMAIL_HOST_USER = config.get('EMAIL', 'host_user')
EMAIL_HOST_PASSWORD = config.get('EMAIL', 'host_password')
EMAIL_USE_SSL = eval(config.get('EMAIL', 'ssl'))
EMAIL_USE_TLS = eval(config.get('EMAIL', 'tls'))
DEFAULT_MAIL = config.get('EMAIL', 'default_mail_dest')
DEFAULT_MAIL_FROM = config.get('EMAIL', 'default_mail_from')

# Contact
DEFAULT_FROM_EMAIL = config.get('EMAIL', 'default_mail_from')
ENVELOPE_EMAIL_RECIPIENTS = [DEFAULT_MAIL]

# Configure crispy-forms
CRISPY_TEMPLATE_PACK = 'bootstrap3'
CRISPY_FAIL_SILENTLY = not DEBUG

# More variables from config.ini
LOG_PATH = config.get('PATHS', 'log')
DATA_PATH = config.get('PATHS', 'data')

# Var for production
if not DEBUG:
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    SERVER_MAIL = config.get('DEFAULT', 'servermail')
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

# End
log.debug("Settings done")
