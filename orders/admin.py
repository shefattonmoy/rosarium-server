from django.contrib import admin
from . import models

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ['all_products_name', 'customer_name', 'order_types', 'order_status', 'address', 'time', 'cancel']
    
    def customer_name(self, obj):
        return obj.customer.user.first_name
    
    def all_products_name(self, obj):
        return obj.all_products.user.first_name
    
admin.site.register(models.Order, OrderAdmin)
