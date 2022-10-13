from rest_framework import serializers

from category.models import Category
from .models import Product

class ProductListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    class Meta:
        m=model = Product
        fields = ('owner','title','price','images')

class ProductDetailSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    category = serializers.PrimaryKeyRelatedField(required=True,queryset= Category.objects.all())    #БЕЗ КАТЕГОРИИ НЕ МОЖЕМ ТЕПЕРЬ СОЗДАТЬ ПРОДУКТ

    class Meta:
        model = Product
        fields = '__all__'