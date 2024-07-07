from rest_framework import serializers
from . import models

class AllProductSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many = False)
    color = serializers.StringRelatedField(many = True)
    category = serializers.StringRelatedField(many = True)
    receiving_time = serializers.StringRelatedField(many = True)
    class Meta:
        model = models.AllProduct
        fields = '__all__'
        
class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Color
        fields = '__all__'
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'
        
class ReceivingTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ReceivingTime
        fields = '__all__'
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'