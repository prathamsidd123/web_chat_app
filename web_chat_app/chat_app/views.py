from django.shortcuts import render
from .models import Room,Message
def room(request):
    data = Room.objects.all()
    return render(request,"rooms.html",{"data":data})


def room_view(request,slug):
    room_name=Room.objects.get(slug=slug).name
    messages=Message.objects.filter(room=Room.objects.get(slug=slug))
    
    return render(request, "room.html",{"room_name":room_name,"slug":slug,'messages':messages})