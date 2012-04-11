from django.contrib import admin
from fruit.app.models import *

class PriceInline(admin.TabularInline):
    model = PriceInfo

class FruitAdmin(admin.ModelAdmin):
    inlines = [PriceInline,]

class OrderItemInline(admin.TabularInline):
    model = OrderItem

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline,]

class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Fruit, FruitAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Post, PostAdmin)