from rest_framework import serializers
from .models import Category, Product, Extra, Drink


class ExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extra
        fields = ['extra_name', 'extra_price']


class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['drink_name', 'drink_price']


class ProductSerializer(serializers.ModelSerializer):
    extra = ExtraSerializer(many=True, read_only=True)
    drink = DrinkSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['product_name', 'description', 'image', 'product_price', 'extra', 'drink']


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']


class CategoryDetailSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['products']
