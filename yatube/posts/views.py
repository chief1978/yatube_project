from django.shortcuts import render, get_object_or_404
from .models import Post, Group


def index(request):
    """
    View для главной страница проекта.
    Выводит 10 последних сообщений
    """
    # используем template
    template = 'posts/index.html'

    # заголовок страница = название сообшества
    title = 'Это главная страница проекта Yatube'

    # Выгружаем последние 10 постов
    posts = Post.objects.order_by('-pub_date')[:10]

    # подготовливаем контекст для страницы, заголовок и сами посты
    context = {
        'title': title,
        'posts': posts,
    }
    # рендерим ...
    return render(request, template, context)


def group_posts(request, slug):
    """
    View для просмотра постов конкретного сообщества.
    Принимает на входе переменную slug
    уникальный идентификатор, он же url по кторому будут доступны
    к просмотру сообщения сообщества.
    Для просмотра доступны 10 последних сообщений сообщества
    """
    # Функция get_object_or_404 получает по заданным критериям объект
    # из базы данных или возвращает сообщение об ошибке, если объект не найден.
    # В нашем случае в переменную group будут переданы объекты модели Group,
    # поле slug у которых соответствует значению slug в запросе
    group = get_object_or_404(Group, slug=slug)

    # Метод .filter позволяет ограничить поиск по критериям.
    # Это аналог добавления
    # условия WHERE group_id = {group_id}
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]

    # заголовок страница = название сообшества
    title = group.__str__

    # используем template
    template = 'posts/group_list.html'

    # подготовливаем контекст для страницы, заголовок и сами посты
    context = {
        'title': title,
        'posts': posts,
    }
    # рендерим ...
    return render(request, template, context)
