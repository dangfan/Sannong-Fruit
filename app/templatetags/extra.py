# coding: utf-8

from django import template
import re

register = template.Library()

@register.filter
def fruits(order):
    return u'、'.join(item.fruit.name for item in order.items.all())

@register.filter
def amount(order):
    sum = 0
    for item in order.items.all():
        price = float(re.search(r'[\d\.]+', item.price).group())
        sum += price * item.amount
    return sum