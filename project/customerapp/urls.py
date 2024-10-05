from django.urls import path
from . import views

urlpatterns = [

     path('', views.customerhomepage, name='customerhomepage'),
     path('categories', views.categories, name='categories'),
     path('homeaccessories', views.homeaccessories, name='homeaccessories'),
     path('mobiles', views.mobiles, name='mobiles'),
     path('shirts', views.shirts, name='shirts'),

]
