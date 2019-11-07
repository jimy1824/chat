from channels.routing import ProtocolTypeRouter
from django.urls import re_path
from . import consumers

chat_urlpatterns = [
    re_path(r'ws/chat/(?P<receiver_id>\w+)/(?P<sender_id>\w+)$', consumers.ChatConsumer),
]
