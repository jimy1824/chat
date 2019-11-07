from django.db import models
from account.models import User
# Create your models here.

class BaseModel(models.Model):
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Chat(BaseModel):
    sender=models.ForeignKey(User,related_name='message_sender' ,on_delete=models.CASCADE)
    receiver=models.ForeignKey(User,related_name='message_receiver', on_delete=models.CASCADE)
    message=models.TextField()
    is_read = models.BooleanField(default=False)