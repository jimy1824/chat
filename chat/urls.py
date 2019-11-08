from django.urls import path
from chat import views
urlpatterns = [
    path('chat/', views.ChatHome.as_view(), name='chat_home'),
    path('chat_box/<int:selected_user_id>', views.ChatInbox.as_view(), name='chat_inbox'),
]
