from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    template = 'posts/index.html'
    return render(request, template)

def group_posts(request, group_name):
    return HttpResponse(f'А теперь посмотрим на посты группы {group_name}')
    
