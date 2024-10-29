"""
ASGI config for gestion_grandeurs project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
import django
from channels.routing import ProtocolTypeRouter

from django.core.asgi import get_asgi_application

from mqtt_topics.consumers import GrandeurMqttConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestion_grandeurs.settings')

django.setup()

# application = get_asgi_application()
application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'mqtt': GrandeurMqttConsumer().as_asgi(),    
})


