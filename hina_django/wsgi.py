"""
WSGI config for hina_django project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

application = get_wsgi_application()
application = DjangoWhiteNoise(application)

#OLD
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'hina_django.settings'

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hina_django.settings")

# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()
