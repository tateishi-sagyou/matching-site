from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path( 'ws/matching/', consumers.ChatConsumer.as_asgi() ),
]
