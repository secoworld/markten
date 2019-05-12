from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#设置博客的类型
class BlogType(models.Model):
    type_name = models.CharField( max_length=50)

    #显示字符的内容
    def __str__(self):
        return self.type_name
    

class Article(models.Model):
    # 文章的标题，作者，发表时间， 修改时间，文章内容，文章分类
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    creat_time = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    content = models.TextField()
    blog_type =  models.ForeignKey(BlogType, on_delete=models.DO_NOTHING) 

    #显示字符的内容
    def __str__(self):
        return self.title

    #定义含义
    class Meta:
        ordering  = ["-creat_time",]  #排序的规则 