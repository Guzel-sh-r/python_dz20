from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=40, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    name = models.CharField(max_length=40, unique=True)
    text = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    # связь с категорией
    # один - много
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # Связь с тегом
    # много - много
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name
