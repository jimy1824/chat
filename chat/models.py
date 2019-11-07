from django.db import models
from account.models import User
from rest_framework import serializers


# Create your models here.

class BaseModel(models.Model):
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Chat(BaseModel):
    sender = models.ForeignKey(User, related_name='message_sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='message_receiver', on_delete=models.CASCADE)
    message = models.TextField()

#
# class UserListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'first_name', 'last_name', 'email', 'gender', 'profile_picture')
#
# #
# class PrivateMessageViewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Chat
#
#     sender = serializers.SerializerMethodField()
#     receiver = serializers.SerializerMethodField()
#
#     def get_sender(self, obj):
#         return UserListSerializer(obj.sender).data
#
#     def get_receiver(self, obj):
#         return UserListSerializer(obj.receiver).data
