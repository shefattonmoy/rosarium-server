from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from . import models
from . import serializers

# Create your views here.

class AllProductViewset(viewsets.ModelViewSet):
    queryset = models.AllProduct.objects.all()
    serializer_class = serializers.AllProductSerializer
    
class ColorViewset(viewsets.ModelViewSet):
    queryset = models.Color.objects.all()
    serializer_class = serializers.ColorSerializer
    
class CategoryViewset(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    
class ReceivingTimeViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = models.ReceivingTime.objects.all()
    serializer_class = serializers.ReceivingTimeSerializer
    
class ReviewViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer