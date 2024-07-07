from django.db import models

# Create your models here.
class FeaturedProduct(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    image = models.ImageField(upload_to = "featured_products/images/")