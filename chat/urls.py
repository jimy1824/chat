from django.urls import path
from chat import views
urlpatterns = [
    path('chat/', views.ChatInbox.as_view(), name='chat_inbox'),
]
