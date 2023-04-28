# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('home/', views.withtemplates),
    path('retificaLonga/maq235/', views.maq235),
    path('retificaLonga/display/', views.maq235),
    path('retificaLonga/template/', views.template)
]
