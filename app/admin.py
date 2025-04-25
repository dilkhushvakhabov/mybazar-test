from django.contrib import admin

from .models.store import Product, Category


admin.site.register(Category)
admin.site.register(Product)