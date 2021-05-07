from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.patient,name='patient'),
    path('success', views.success,name='success'),
]
