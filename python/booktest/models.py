from django.db import models

# Create your models here.


class BookInfo(models.Model):
    # 定义书类
    # 书名
    book_name = models.CharField(max_length=20)
    # 作者
    book_author = models.CharField(max_length=10)
    # 出版日期
    book_date = models.DateField()

    # def __str__(self):
    #     return self.book_name


class HeroInfo(models.Model):
    # 英雄名字
    name = models.CharField(max_length=10)
    # 英雄性别True代表男生false代表女生
    gender = models.BooleanField(default=True)
    # 英雄技能
    comment = models.CharField(max_length=20)
    # 英雄对应的书籍
    hbook = models.ForeignKey('BookInfo')

    def __str__(self):
        return self.name


