"""
Django settings for dbug project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g6z9)!uu!3hu2&d0-37*t$uhn+frrr2*ml8spc#wbyuda4j@#b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'snippets',
    'fibonacci',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'qinspect.middleware.QueryInspectMiddleware',
)

ROOT_URLCONF = 'dbug.urls'

WSGI_APPLICATION = 'dbug.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'no_upload/db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

#################
# Query Inspector
#################

# Whether the Query Inspector should do anything (default: False)
QUERY_INSPECT_ENABLED = True

# Whether to log the stats via Django logging (default: True)
QUERY_INSPECT_LOG_STATS = True

# Whether to add stats headers (default: True)
QUERY_INSPECT_HEADER_STATS = True

# Whether to log duplicate queries (default: False)
QUERY_INSPECT_LOG_QUERIES = True

# Whether to log queries that are above an absolute limit (default: None - disabled)
QUERY_INSPECT_ABSOLUTE_LIMIT = 100  # in milliseconds

# Whether to log queries that are more than X standard deviations above the mean query time (default: None - disabled)
QUERY_INSPECT_STANDARD_DEVIATION_LIMIT = 2

QUERY_LOG_ALL = True

#################
# Logging to disk
#################
# https://docs.djangoproject.com/en/1.7/topics/logging/#topic-logging-parts-loggers

LOGGING = {
    'version': 1,
    # 'disable_existing_loggers': True,
    # 'root': {
    #     'level': 'DEBUG',
    #     'handlers': ['console', ],   # Here you define the active handlers
    # },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'generic': {
            'format': '%(asctime)s %(module)s [%(process)d] [%(levelname)s] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
            'class': 'logging.Formatter',
        },
    },
    'handlers': {
        # 'mail_admins': {
        #     'level': 'ERROR',
        #     'filters': ['require_debug_false'],
        #     'class': 'django.utils.log.AdminEmailHandler'
        # },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'error_file': {
            'class': 'logging.FileHandler',
            'formatter': 'generic',
            'filename': os.path.join(BASE_DIR, 'no_upload/django_logger.error.log'),
        },
        'access_file': {
            'class': 'logging.FileHandler',
            'formatter': 'generic',
            'filename': os.path.join(BASE_DIR, 'no_upload/django_logger.access.log'),
        },
        # 'celery': {
        #     'level': 'INFO',
        #     'class': 'logging.FileHandler',
        #     'filename': os.path.join(LOG_DIR, 'django_celery.error.log'),
        #     'formatter': 'generic',
        # },
    },
    'loggers': {
        # 'django.request': {
        #     'handlers': ['mail_admins'],
        #     'level': 'ERROR',
        #     'propagate': True,
        # },
        # 'django.db.backends': {
        #     'level': 'ERROR',
        #     'handlers': ['console'],
        #     'propagate': False,
        # },
        'snippets': {
            'handlers': ['console', ],
            'level': 'DEBUG',
        },
        'qinspect': {
            'handlers': ['console',],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}
