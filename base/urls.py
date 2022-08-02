from django.urls import path
from . import views # we are calling another file

urlpatterns = [ #this is another  url patterns it contains urls
    path("",views.home,name = "home"),
    path("room/<str:pk>/",views.room,name = "room" ), #room is url  to move next page
    path("create-room/",views.createRoom,name = "create-room"),
    path("update-room/<str:pk>",views.updateRoom,name = "update-room"),
    path("delete-room/<str:pk>",views.deleteRoom,name = "delete-room"),
    path("login/",views.LogInPage,name = "login"),
    path("logout/",views.LogOutPage,name = "logout"),
    path("register/",views.registerPage,name = "register"),
    path("delete-message/<str:pk>",views.deleteMassage,name = "delete-massage"),
]