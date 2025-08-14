from django.contrib import admin
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    # Pour être sûr de ne rien oublier, on affiche TOUS les champs
    fields = ['name', 'price', 'image', 'category']
    list_display = ['name', 'price', 'category']

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
