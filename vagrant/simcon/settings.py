"""
Django settings for simcon project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SERVER_EMAIL = 'django@pdx.edu'

SITE_ID = "http://127.0.0.1:8000"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xb5@_&)+qo7edldwq95!^wdd)a&%5g3(d!2ud4-!_ta@6b-t(3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True
TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'), )

ALLOWED_HOSTS = []

FIXTURE_DIRS = (os.path.join(BASE_DIR, 'fixtures'), )

# Application definition

INSTALLED_APPS = (
    'simcon',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tinymce',  # for rich text embeds
    #'debug_toolbar',
)

MIDDLEWARE_CLASSES = (
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(os.getcwd(), MEDIA_URL)       
#absolute file system path to directory containing audio files
#part of response app model.  Must be different than STATIC_ROOT	-Griff

ROOT_URLCONF = 'simcon.urls'

WSGI_APPLICATION = 'simcon.wsgi.application'

# Password Recovery Options
# FIXME: Some set of these need to be populated in production
#    EMAIL_HOST = 'localhost'
#    EMAIL_PORT = 1025
#    EMAIL_HOST_USER = ''
#    EMAIL_HOST_PASSWORD = ''
#    EMAIL_USE_TLS = False
#    DEFAULT_FROM_EMAIL = 'noreply@pdx.edu'

# In a debug environment, we can use a dummy smptd
# Run the following in a separate terminal in your VM:
# $ python -m smtpd -n -c DebuggingServer localhost:1025
if DEBUG:
    EMAIL_HOST = 'localhost'
    EMAIL_PORT = 1025
    EMAIL_HOST_USER = ''
    EMAIL_HOST_PASSWORD = ''
    EMAIL_USE_TLS = False
    DEFAULT_FROM_EMAIL = 'noreply@pdx.edu'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

AUTH_PROFILE_MODULE = 'simcon.researcher'

#DEBUG_TOOLBAR_PATCH_SETTINGS = False

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)

from django.core.urlresolvers import reverse_lazy
LOGIN_URL=reverse_lazy('login')

#Logging functionality
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'null': {
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler',
        },
        'logfile': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR + "/logfile",
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'standard',
        },
        'console':{
            'level':'INFO',
            'class':'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        'django': {
            'handlers':['console'],
            'propagate': True,
            'level':'WARN',
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'simcon': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
        },
    }
}

