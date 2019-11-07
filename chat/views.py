from django.shortcuts import render
from django.views import View
from account.models import User


class ChatInbox(View):
    template_name = 'chat_box.html'

    def get(self, request, *args, **kwargs):
        reciever_id = int(kwargs.get('receiver_id'))
        sender_id = self.request.user.id
        return render(request, self.template_name, context={'reciever_id': reciever_id, 'sender_id': sender_id})


class UsersList(View):
    template_name = 'users_list.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={'users': User.objects.all()})
