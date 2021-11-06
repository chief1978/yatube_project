"""posts app URL Configuration
"""
from django.urls import path

from . import views

# Задаём namespace 
app_name = 'posts'

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
    # Посты сообщества slug
    path('group/<slug:slug>/', views.group_posts, name='slug'),
]
