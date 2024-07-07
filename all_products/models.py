from django.db import models
from django.contrib.auth.models import User
from customer.models import Customer

# Create your models here.
class Color(models.Model):
    name = models.CharField(max_length = 30)
    slug = models.SlugField(max_length = 30)
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length = 30)
    slug = models.SlugField(max_length = 30)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"
    
class ReceivingTime(models.Model):
    name = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.name
    
class AllProduct(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(upload_to = "all_products/images/")
    category = models.ManyToManyField(Category)
    color = models.ManyToManyField(Color)
    receiving_time = models.ManyToManyField(ReceivingTime)
    price = models.IntegerField()
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
STAR_CHOICES = [
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
]
    
class Review(models.Model):
    reviewer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    product = models.ForeignKey(AllProduct, on_delete = models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    rating = models.CharField(choices = STAR_CHOICES, max_length = 10)
    
    def __str__(self):
        return f"Customer: {self.reviewer.user.first_name} ; Product {self.product.user.first_name}"