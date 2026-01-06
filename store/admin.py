from django.contrib import admin
from .models import Category, Product, ProductImage

# Register your models here.
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "price", "is_active")
    inlines = [ProductImageInline]
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
