from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model() 

class Group(models.Model):
    # Название сообщества
    title = models.CharField(max_length=200)
    # Адрес сообщества
    slug = models.SlugField(max_length=100)
    # Описание сообщества
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    group = models.ForeignKey(
        Group, 
        on_delete=models.CASCADE, 
        related_name='posts', 
        blank=True, 
        null=True
    )