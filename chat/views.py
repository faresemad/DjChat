from django.shortcuts import render
from .models import ChatRoom, Messages
# Create your views here.

def index(request):
    rooms = ChatRoom.objects.all()
    return render(request, 'chat/index.html', {'rooms': rooms})

def room(request, room_name):
    room = ChatRoom.objects.get_or_create(name=room_name)
    try:
        messages = Messages.objects.filter(room=room)
    except:
        messages = []
    return render(request, 'chat/room.html', {'room': room})