from channels.routing import ProtocolTypeRouter
from django.urls import re_path
from . import consumers

chat_urlpatterns = [
    # Empty for now (http->django views is added by default)
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer),
]