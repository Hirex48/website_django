from django.contrib import admin
from .models import Category, Products

class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'price']
    list_filter = ['price', 'name']
    search_fields = ['name']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name', 'id']
    search_fields = ['name']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Products, ProductsAdmin)