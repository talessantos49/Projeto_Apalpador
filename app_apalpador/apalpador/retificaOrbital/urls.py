from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('retificaOrbital/display/', views.maq15),
    path('retificaOrbital/template/', views.maq15),
    path('retificaOrbital/maq15', views.maq15 )
]
