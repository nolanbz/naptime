from django.urls import path
from . import views

urlpatterns = [
    path('', views.channel_list, name='channel_list'),
    path('channel/<int:pk>/', views.channel_detail, name='channel_detail'),
]