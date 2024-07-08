from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers

# Create your views here.
class FeaturedProductViewset(viewsets.ModelViewSet):
    queryset = models.FeaturedProduct.objects.all()
    serializer_class = serializers.FeaturedProductSerializer