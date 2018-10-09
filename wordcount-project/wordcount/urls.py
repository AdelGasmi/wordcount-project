
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('about/', views.about, name='about'),
    #We include name for action so that we do not have problems of mapping 
    path('count/', views.count, name='count'),
]
