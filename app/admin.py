from django.contrib import admin
from fruit.app.models import Fruit, PriceInfo

class PriceInline(admin.TabularInline):
    model = PriceInfo

class FruitAdmin(admin.ModelAdmin):
    inlines = [PriceInline,]

admin.site.register(Fruit, FruitAdmin)