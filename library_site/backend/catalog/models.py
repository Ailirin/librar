from django.db import models

class Book(models.Model):
    title = models.CharField("Название", max_length=200)
    author = models.CharField("Автор", max_length=100)
    genre = models.CharField("Жанр", max_length=50)
    year_published = models.PositiveIntegerField("Год издания")
    description = models.TextField("Описание", blank=True)

    def __str__(self):
        return self.title