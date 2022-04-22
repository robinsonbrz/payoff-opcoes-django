from django import views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('2', views.home2, name='home2'),
]
