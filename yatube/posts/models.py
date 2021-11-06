from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Group(models.Model):
    # Класс - сообщества

    # Название сообщества
    title = models.CharField(max_length=200, unique=True)
    # уникальное наименование, он же url сообщества
    slug = models.SlugField(max_length=100, unique=True)
    # Описание сообщества, может отсуствовать
    description = models.TextField(blank=True, null=True)

    # __str__ будет возвращать название сообщества
    def __str__(self):
        return self.title


class Post(models.Model):
    # Класс - посты

    # Текст поста
    text = models.TextField()
    # Дата публикации поста
    pub_date = models.DateTimeField(auto_now_add=True)
    # Автор поста
    # Привязываемся к таблице Users
    # При удалении пользователя удаляем и посты
    # Создаём обратную связь с именем posts
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    # Сообщество в котором опубликован пост
    # Привязываемся к таблице group
    # При удалении группы удаляем и посты
    # Создаём обратную связь с именем posts
    # Может отсуствовать
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name='posts',
        blank=True,
        null=True
    )
