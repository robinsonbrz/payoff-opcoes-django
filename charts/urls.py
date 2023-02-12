from django import views
from django.urls import path

from . import views
from .views import AjaxCalculoHandler , home


urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.home, name='home'),
    path('ajaxCalculoHandler', AjaxCalculoHandler.as_view(), name='ajaxCalculoHandler'),
]
