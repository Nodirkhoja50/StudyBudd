"""djangobudy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include #path for includes only urls
                                      #includes for call another packeges's file



urlpatterns = [  #urlpatterns includes only urls
    path('admin/', admin.site.urls), #maybe it is kind of doing nothing
    path('',include('base.urls')), #include function is calling another packeges file which is contain urls
]
