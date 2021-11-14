from django.urls import path

from . import views

urlpatterns = [
    path('', views., name='home'),
    path('<str:e_name>/'o, views.detail, name='detail')
]
