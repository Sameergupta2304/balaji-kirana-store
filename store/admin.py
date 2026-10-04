from django.contrib import admin

# Register your models here.
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'available',
        'is_featured',
        'updated_at',
    )

    list_filter = (
        'category',
        'available',
        'is_featured'
    )

    search_fields = (
        'name',
        'description',
    )