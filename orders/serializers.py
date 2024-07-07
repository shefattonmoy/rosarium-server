from rest_framework import serializers
from . import models

class OrderSerializer(serializers.ModelSerializer):
    time = serializers.StringRelatedField(many = False)
    customer = serializers.StringRelatedField(many = False)
    all_products = serializers.StringRelatedField(many = False)
    class Meta:
        model = models.Order
        fields = '__all__'