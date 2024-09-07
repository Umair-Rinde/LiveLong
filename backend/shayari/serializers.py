from rest_framework import serializers
from .models import Shayaries


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Shayaries
        fields = '__all__'


class ShayariesGetSerializer(serializers.ModelSerializer):
    category= CategorySerializer
    class Meta:
        model = Shayaries
        fields = '__all__'


class ShayariesPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shayaries
        fields = '__all__'


class CategoryShayariSerializer(serializers.ModelSerializer):
    shayaries=ShayariesPostSerializer()
    class Meta:
        model = Shayaries
        fields = '__all__'