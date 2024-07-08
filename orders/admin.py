from django.contrib import admin
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from . import models

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ['all_products_name', 'customer_name', 'order_types', 'order_status', 'address', 'time', 'cancel']
    
    def customer_name(self, obj):
        return obj.customer.user.first_name
    
    def all_products_name(self, obj):
        return obj.all_products.user.first_name
    
    def save_model(self, request, obj, form, change):
        obj.save()
        if obj.order_status == "Confirmed" and obj.order_types == "Home Delivery":
            email_subject = "Your home delivery order is confirmed."
            email_body = render_to_string('admin_email.html', {'customer' : obj.customer.user, 'all_products' : obj.all_products})
            print(email_body)
            email = EmailMultiAlternatives(email_subject , '', to=[obj.customer.user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()
    
admin.site.register(models.Order, OrderAdmin)
