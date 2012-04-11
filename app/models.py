# coding:utf-8
from django.contrib.auth.models import User
from django.db import models

class PriceInfo(models.Model):
    price = models.CharField(max_length=20, verbose_name=u'价格')
    date = models.DateField(verbose_name=u'采集日期')
    fruit = models.ForeignKey('Fruit', related_name='price_list')

    def __unicode__(self):
        return u'价格信息'

class Fruit(models.Model):
    name = models.CharField(max_length=10, unique=True, db_index=True, verbose_name=u'名称')
    introduction = models.TextField(verbose_name=u'简介')
    picture = models.ImageField(upload_to='static/photos', verbose_name=u'照片')

    def __unicode__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User)
    date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return u'订单：%d - %s' % (self.id, self.user.username)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items')
    fruit = models.ForeignKey(Fruit, related_name='+', verbose_name=u'水果')
    price = models.CharField(max_length=20, verbose_name=u'价格')
    amount = models.IntegerField(verbose_name=u'数量')

class Post(models.Model):
    title = models.CharField(max_length=30, verbose_name=u'标题')
    content = models.TextField(verbose_name=u'正文')
    date = models.DateField(auto_now_add=True, db_index=True)

    def __unicode__(self):
        return self.title