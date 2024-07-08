from django.db import models
from customer.models import Customer
from all_products.models import AllProduct, ReceivingTime

# Create your models here.

ORDER_STATUS = [
    ('Pending', 'Pending'),
    ('Confirmed', 'Confirmed'),
    ('Processing', 'Processing'),
    ('Completed', 'Completed'),
]

ORDER_TYPES = [
    ('Home Delivery', 'Home Delivery'),
    ('Pick-Up', 'Pick-Up'),
]

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    all_products = models.ForeignKey(AllProduct, on_delete = models.CASCADE)
    order_types = models.CharField(choices = ORDER_TYPES, max_length = 30, default = "Home Delivery")
    order_status = models.CharField(choices = ORDER_STATUS, max_length = 30, default = "Pending")
    address = models.TextField()
    time = models.ForeignKey(ReceivingTime, on_delete = models.CASCADE)
    cancel = models.BooleanField(default = False)
    
    def __str__(self):
        return f"Product : {self.all_products.user.first_name}, Customer: {self.customer.user.first_name}"