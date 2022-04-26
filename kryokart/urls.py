from django.contrib import admin
from django.urls import path
from . import views #Relativ import av viewsfunksjonen

appname = "kryokart"
urlpatterns = [
    path('', views.index, name='index'),
    path('post/', views.jsonGPS, name='post'),
    path('hook/', views.hook, name='webhook')
]