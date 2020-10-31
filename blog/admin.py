from django.contrib import admin
from .models import Post

admin.site.register(Post)  #Чтобы наша модель стала доступна на странице администрирования

# Register your models here.
