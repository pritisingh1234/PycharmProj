from django.urls import path

from . import views

urlpatterns = [
    path('', views.hello, name='home'),
    path('<str:e_name>/', views.detail, name='detail')
]
