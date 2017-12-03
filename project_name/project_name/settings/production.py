from {{ project_name }}.settings import *  # flake8: NOQA
import os
import dj_database_url


ALLOWED_HOSTS = ['*']

DEBUG = False

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_SECONDS = 31536000
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY') or SECRET_KEY


############
# NewRelic #
############

ENABLE_NEWRELIC_WSGI = True
NEWRELIC_ENVIRONMENT = 'production'


##################
# Raven (Sentry) #
##################
# https://docs.getsentry.com/hosted/clients/python/integrations/django/

INSTALLED_APPS += [
    'raven.contrib.django.raven_compat',
]

RAVEN_CONFIG = {
    'dsn': os.environ.get("SENTRY_DSN", ""),
    'release': os.environ.get("SENTRY_RELEASE",""),
    'environment': 'production',
}

LOGGING.update({
    'root': {
        'handlers': ['sentry'],
        'level': 'WARNING',
    }
})


####################
# Your application #
####################

DATABASES = {
    'default': dj_database_url.config()
}
