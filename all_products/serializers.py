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
    reviewer_name = serializers.SerializerMethodField()
    reviewer_image = serializers.SerializerMethodField()
    class Meta:
        model = models.Review
        fields = '__all__'
        
    def get_reviewer_name(self, obj):
        return obj.reviewer.user.first_name
    
    def get_reviewer_image(self, obj):
        if obj.reviewer.image:
            return obj.reviewer.image.url
        return None