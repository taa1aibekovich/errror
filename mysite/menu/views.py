from rest_framework import viewsets, filters
from .models import Category, Product, Extra, Drink
from .serializers import CategoryListSerializer, ProductSerializer, ExtraSerializer, DrinkSerializer,  CategoryDetailSerializer


class CategoryListViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['category_name']


class CategoryDetailViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['product_name', 'description']


class ExtraViewSet(viewsets.ModelViewSet):
    queryset = Extra.objects.all()
    serializer_class = ExtraSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['extra_name']


class DrinkViewSet(viewsets.ModelViewSet):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['drinks_name']
