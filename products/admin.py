from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(Category)


class ProductImageAdmin(admin.StackedInline):
    model = ProductImage

class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name','price']
    inlines = [ProductImageAdmin]

admin.site.register(ColorVariant)
admin.site.register(SizeVariant)
class ColorVariantAdmin(admin.ModelAdmin):
    list_display = ['color_name','price']
    model = ColorVariant


class SizeVariantAdmin(admin.ModelAdmin):
    list_display = ['size_name','price']
    model = SizeVariant
       


admin.site.register(Product,ProductAdmin)

admin.site.register(ProductImage)