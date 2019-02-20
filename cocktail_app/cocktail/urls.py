"""cocktail_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from . import views
from django.conf.urls import url,include


urlpatterns = [
     path('upload/', views.upload, name='upload'),
     path('top/', views.top, name='top'),
     path('search/', views.search, name='search'),
     path('request/', views.request, name='request'),
     path('registration/', views.registration, name='registration'),
     path('record/', views.record, name='record'),
]
