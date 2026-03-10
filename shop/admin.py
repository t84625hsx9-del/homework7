from django.contrib import admin
from .models import Product

@admin.action(description='Скидка 10%')
def apply_discount(modeladmin, request, queryset):
    for product in queryset:
        product.price *= 0.9
        product.save()

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at') # Поля в списке
    list_filter = ('created_at',)                  # Фильтры справа
    search_fields = ('name', 'description')        # Поиск
    actions = [apply_discount]