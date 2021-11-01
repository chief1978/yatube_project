from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Главная страница блога пока еще убога')

def group_posts(request, group_name):
    return HttpResponse(f'А теперь посмотрим на посты группы {group_name}')
    
