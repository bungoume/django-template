"""
WSGI config for {{ project_name }} project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""

import os

from django.conf import settings
from django.core.wsgi import get_wsgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings")

application = get_wsgi_application()

if settings.ENABLE_NEWRELIC_WSGI:
    import newrelic.agent
    newrelic.agent.initialize(os.path.join(settings.BASE_DIR, 'newrelic.ini'),
                              environment=getattr(settings, 'NEWRELIC_ENVIRONMENT', None))
    application = newrelic.agent.wsgi_application()(application)
