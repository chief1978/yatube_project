"""posts app URL Configuration
"""
from django.urls import path

from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    # Посты с фильтром по имени группы
    path('group/<slug:group_name>/', views.group_posts),
]
