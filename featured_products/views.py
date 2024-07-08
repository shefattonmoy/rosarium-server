from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny

@api_view(['GET'])
@authentication_classes([])
@permission_classes([AllowAny])

# Create your views here.
class FeaturedProductViewset(viewsets.ModelViewSet):
    queryset = models.FeaturedProduct.objects.all()
    serializer_class = serializers.FeaturedProductSerializer