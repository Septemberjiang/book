from django.db import models


class BookCategory(models.Model):

    name = models.CharField("类别名称",max_length=32)

    class Meta:
        db_table = "BookCategory"

class BookName(models.Model):

    name = models.CharField("书籍名字",max_length=32)
    author  = models.CharField("作者",max_length=32)
    images = models.CharField("书籍封面",max_length=32)
    category = models.ForeignKey(BookCategory,on_delete=BookCategory)

    class Meta:
        db_table = "BookName"

class BookContent(models.Model):
    sheet = models.CharField("章节名称",max_length=32)
    content = models.TextField("章节内容")

    class Meta:
        db_table = "BookContent"


class User(models.Model):
    username = models.CharField("用户名",max_length=32)
    password = models.CharField("用户密码",max_length=61)

    class Meta:
        db_table = "User"

# 支付宝支付用
class BookShoppingOrdering(models.Model):
    order_number = models.CharField(max_length=64)
    status_choices = ((0, '未支付'), (1, '已支付'))
    order_status = models.IntegerField(choices=status_choices, default=0)
    goods = models.ForeignKey(to='BookName', on_delete=models.CASCADE)