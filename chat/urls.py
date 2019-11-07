from django.urls import path
from chat import views

urlpatterns = [
    path('chat/<int:receiver_id>/', views.ChatInbox.as_view(), name='chat_inbox'),
    path('users_list/', views.UsersList.as_view(), name='users_list')
]
