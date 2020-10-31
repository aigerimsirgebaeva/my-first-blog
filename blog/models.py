from django.conf import settings #from ... import открывает доступ к коду из других файлов 
from django.db import models
from django.utils import timezone


class Post(models.Model): #эта строка определяет наш обьект
    #class — это специальное ключевое слово для определения объектов.
    #Post — это имя нашей модели, мы можем поменять его при желании
    #(специальные знаки и пробелы использовать нельзя).
    #Всегда начинай имена классов с прописной буквы.
    #models.Model означает, что объект Post является моделью Django,
    #так Django поймет, что он должен сохранить его в базу данных.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
