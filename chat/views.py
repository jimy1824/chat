from django.shortcuts import render
from django.views import View
from account.models import User


class ChatInbox(View):
    template_name='chat_box.html'

    def get(self,request,*args,**kwargs):
        return render(request,self.template_name,context={'users':User.objects.all()})