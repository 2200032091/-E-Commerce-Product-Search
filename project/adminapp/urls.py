from django import views
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('adminapp/',views.adminhomepage,name='adminhomepage'),
    path('about', views.about, name='about'),
    path('shopnow', views.shopnow, name='shopnow'),
    path('contact', views.contact, name='contact'),
    path('login', views.login, name='login'),
]
