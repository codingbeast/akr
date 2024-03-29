"""
ASGI config for projectalfa project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from whitenoise.django import DjangoWhiteNoise
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projectalfa.settings')

application = get_asgi_application()
application = DjangoWhiteNoise(application)

