from django.contrib import admin
from .models import Product, Category

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    # sorts 
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image'
    )

    # must be a tuple, sorts the products by defined key
    # to apply reverse order add - before the key
    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',

    )

# after creating models we need to register them to see it
# new classes needs to be registered as well
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
