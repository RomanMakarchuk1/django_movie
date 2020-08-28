from django.db import models

class Category(models.Model):
    """Categories"""
    name = models.CharField('Категория', max_length=160)
    desc = models.TextField('Описание')
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Actor(models.Model):
    """Actors and directors"""

    name = models.CharField('Имя', max_length=160)
    age = models.PositiveSmallIntegerField('Возраст', default=0)
    desc = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='actors/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Актеры и режиссеры'
        verbose_name_plural = 'Актеры и режиссеры'


class Genre(models.Model):
    """Genres"""
    name = models.CharField('Имя', max_length=160)
    desc = models.TextField('Описание')
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанр'

