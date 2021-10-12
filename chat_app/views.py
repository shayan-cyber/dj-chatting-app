from django.shortcuts import render, redirect
import django
django.setup()
from . models import *
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    users = User.objects.all()
    return render(request, 'home.html', {
        'users': users,
        
    })


def chat_room(request, username):
    if User.objects.get(username=username).id == request.user.id:
        return redirect('/')
    else:
        chat_group = Chat_group.objects.filter(participants__in = [User.objects.get(username=username), request.user])
        if chat_group:
            chat_group = chat_group[0]
            print("exists")
        else:
            chat_group = Chat_group.objects.create()
            chat_group.participants.add(User.objects.get(username=username))
            chat_group.participants.add(request.user)
        print(chat_group)
        chats = Chat.objects.filter(group= chat_group)

        return render(request, 'chat_room.html', {
            'chats':chats,
            'chat_group':chat_group
        })