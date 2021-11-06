"""posts app URL Configuration
"""
from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
    # Посты с фильтром по имени группы
    path('group/<slug:group_name>/', views.group_posts, name='group_posts'),
]
