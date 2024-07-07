from rest_framework import serializers
from . import models

class FeaturedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FeaturedProduct
        fields = '__all__'