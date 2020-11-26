from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(verbose_name='文章标题',
                             max_length=100)
    body = models.TextField(verbose_name='文章内容')
    author = models.CharField(verbose_name='作者', default='sing', max_length=100)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    '''
    CREATE TABLE "blogs"
    ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "title" varchar(100) NOT NULL,
    "body" text NOT NULL,
    "author" varchar(100) NOT NULL,
    "created_time" datetime NOT NULL,
    "update_time" datetime NOT NULL
    );
    '''
    class Meta:

        db_table = 'articles'
        verbose_name = '博客文章'
        verbose_name_plural = '博客文章列表'

    def __str__(self):
        return self.title
