from django.core.management.base import BaseCommand
from ai_app.models import Category, Tag, Post
import pandas as pd
import openpyxl

class Command(BaseCommand):

    def handle(self, *args, **options):

        excel_data = pd.read_excel("post.xlsx")
        data = pd.DataFrame(excel_data, columns=["Заголовок поста", "Текст поста", "Категория", "Тег"])
        for i in range(data.shape[0]):
            category = Category.objects.get_or_create(name=data.values[i][2], description="")
            id_category = category[0].id

            post = Post.objects.get_or_create(name=data.values[i][0], text=data.values[i][1], category=category[0])

            list_tags = data.values[i][3].split(",")
            post[0].tags.clear()
            for tag in list_tags:
                tag_obj = Tag.objects.get_or_create(name=tag.strip())
                post[0].tags.add(tag_obj[0])








        # Выбираем все категории
        # categories = Category.objects.all()
        # print(categories)
        # print(type(categories))
        # for item in categories:
        #     print(item)
        #     print(item.name)
        #     print(type(item))

        # Выбираем одну категорию
        # category = Category.objects.get(name="Кейсы")
        # print(category)
        # print(type(category))

        # Несколько
        # category = Category.objects.filter(name="Кейсы")
        # print(category)
        # print(type(category))

        # Первый пост
        # post = Post.objects.first()
        # print(post)

        # Связанные поля
        # ForeignKey
        # print(post.category)
        # print(type(post.category))
        # print(post.category.name)
        # ManyToMany
        # print(post.tags.all())
        # print(post.tags.first())
        # print(post.tags.first().name)
        # print(type(post.tags.first()))
        # print(post.tags.filter(name="чат боты"))

        # Создание
        # Category.objects.create(name="Воронка", description="")

        # Изменение
        # category = Category.objects.get(name="Воронка")
        # category.name = "Воронка продаж"
        # category.save()

        # Удаление
        # Можно одну,
        # category.delete()
        # можно несколько
        # Category.objects.all().delete()

