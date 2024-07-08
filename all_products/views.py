from django.shortcuts import render
from rest_framework import viewsets, pagination, filters
from rest_framework.permissions import  IsAuthenticatedOrReadOnly
from . import models
from . import serializers

# Create your views here.

class AllProductPagination(pagination.PageNumberPagination):
    page_size = 3
    page_size_query_param = page_size
    max_page_size = 100

class AllProductViewset(viewsets.ModelViewSet):
    queryset = models.AllProduct.objects.all()
    serializer_class = serializers.AllProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'email']
    pagination_class = AllProductPagination
    
class ColorViewset(viewsets.ModelViewSet):
    queryset = models.Color.objects.all()
    serializer_class = serializers.ColorSerializer
    
class CategoryViewset(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    
class ReceivingTimeForSpecificProduct(filters.BaseFilterBackend):
    def filter_queryset(self, request, query_set, view):
        all_products_id = request.query_params.get("all_products_id")
        if all_products_id:
            return query_set.filter(allproduct = all_products_id)
        return query_set
    
class ReceivingTimeViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = models.ReceivingTime.objects.all()
    serializer_class = serializers.ReceivingTimeSerializer
    filter_backends = [ReceivingTimeForSpecificProduct]
    
class ReviewViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    
