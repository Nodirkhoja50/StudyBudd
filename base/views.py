from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import RoomForm
from django.db.models import Q
from .models import Room,Topic,Message
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse #we are importing HttpResponse
#this is functions for the viewing and we are gonna call them in urls pattern
'''rooms = [
    {"id" : 1,"name" : "Nodirkhuja"},
    {"id" : 2,"name" : "None"},
    {"id" : 3,"name" : "None2"},
]'''
def home(request): #it accessepts request
   # return HttpResponse("Home Page") #HttpResponse for response to web

     topics = Topic.objects.all()
     q = request.GET.get("q") if request.GET.get('q') != None else ""
     rooms = Room.objects.filter(Q(topic__name__icontains = q) |
                                 Q(name__icontains = q) |
                                 Q(description__icontains = q))
     #rooms = Room.objects.all()
     room_massages = Message.objects.all()
     room_count = rooms.count()
     room_massages = Message.objects.filter(Q(room__topic__name__icontains=q))
     context = {"rooms" : rooms,"topics":topics,"room_count":room_count,"room_massages":room_massages}
     return render(request, 'base/home.html',context)
def room(request, pk):
    # return HttpResponse("ROOM") #HttpResponse for response to web
    room = Room.objects.get(id = pk)
    room_messages = room.message_set.all().order_by('-created')
    participants = room.participants.all()
    if request.method == 'POST':
        message = Message.objects.create(
            user = request.user,
            room=room,
            body = request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room',pk=room.id)
    context = {"room" : room,"room_messages":room_messages,"participants":participants}
    return render(request, 'base/room.html',context)
# Create your views here.
@login_required(login_url='login')
def createRoom(request):
     form = RoomForm()
     if request.method == 'POST':
        form=RoomForm(request.POST)
     if form.is_valid():
         form.save()
         return redirect("home")
     context = {"form" : form}
     return render(request,'base/room-reform.html',context)
def updateRoom(request,pk):
     room = Room.objects.get(id=pk)
     form = RoomForm(instance=room)
     if request.method == 'POST':
         form = RoomForm(request.POST,instance=room)
     if form.is_valid():
         form.save()
         return redirect("home")
     context= {"form":form}
     return render(request,"base/room-reform.html",context)
def deleteRoom(request,pk):
    room = Room.objects.get(id = pk)

    if request.method == "POST":
        room.delete()
        return redirect("home")
    context = {"obj":room}
    return render(request,"base/deleteRoom.html",context)
def LogInPage(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request,'User does not exist')

        user = authenticate(request,username=username,password =password)
        if user is not None:
            login(request,user)
        return redirect('home')
    return render(request,'base/login_register.html',{'page':page})
def LogOutPage(request):
    logout(request)
    return redirect('home')
def registerPage(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"Error occurred during registration")
    context = {"form":form}
    return render(request,"base/login_register.html",context)
def deleteMassage(request,pk):
    message = Message.objects.get(id = pk)
    if request.method == 'POST':
        message.delete()
        return redirect('home')
    context={'obj':message}
    return render(request,'base/deleteRoom.html',context)
