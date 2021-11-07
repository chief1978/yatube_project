from django.shortcuts import get_object_or_404, render

from .models import Group, Post


def index(request):
    """
    View для главной страница проекта.
    Выводит 10 последних сообщений
    """

    template = 'posts/index.html'
    title = 'Это главная страница проекта Yatube'
    posts = Post.objects.all()[:10]
    context = {
        'title': title,
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    """
    View для просмотра постов конкретного сообщества.
    Принимает на входе переменную slug
    уникальный идентификатор, он же url по кторому будут доступны
    к просмотру сообщения сообщества.
    Для просмотра доступны 10 последних сообщений сообщества
    """

    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:10]
    title = str(group)
    template = 'posts/group_list.html'
    context = {
        'title': title,
        'posts': posts,
    }
    return render(request, template, context)
