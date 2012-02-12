"""
WSGI config for {{ project_name }} project.
"""
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings")

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from django.contrib.staticfiles.handlers import StaticFilesHandler
application = StaticFilesHandler(application)
