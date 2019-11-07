from django.shortcuts import render
from django.views import View
from account.models import User
from chat.models import Chat


class ChatHome(View):
    template_name='chat.html'

    def get(self,request,*args,**kwargs):
        all_users=User.objects.filter(is_superuser=False)
        messages_list=Chat.objects.filter(is_read=False)
        return render(request,self.template_name,context={'users':all_users,'messages_list':messages_list})


class ChatInbox(View):
    template_name='chat_box.html'

    def get(self,request,user_id,*args,**kwargs):
        print(user_id,'user_id')
        return render(request,self.template_name,context={'room_name':'room_name'})
