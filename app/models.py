# coding:utf-8

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

