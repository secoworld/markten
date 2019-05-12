from django.contrib import admin
from .models import BlogType, Article

# Register your models here.
#注册博客类型
@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "type_name")

#注册文章类型
@admin.register(Article)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "blog_type", "author", "creat_time", "last_update")