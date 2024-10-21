from django.urls import path
from .views import (
    CategoryListViewSet,
    CategoryDetailViewSet,
    ProductViewSet,
    ExtraViewSet,
    DrinkViewSet,
)

urlpatterns = [

    path('', CategoryListViewSet.as_view({'get': 'list'}), name='category_list'),
    path('<int:pk>/', CategoryDetailViewSet.as_view({'get': 'retrieve'}), name='category_detail'),


    path('products/', ProductViewSet.as_view({'get': 'list', 'post': 'create'}), name='product_list'),
    path('products/<int:pk>/', ProductViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='product_detail'),


    path('extras/', ExtraViewSet.as_view({'get': 'list', 'post': 'create'}), name='extra_list'),
    path('extras/<int:pk>/', ExtraViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='extra_detail'),


    path('drinks/', DrinkViewSet.as_view({'get': 'list', 'post': 'create'}), name='drink_list'),
    path('drinks/<int:pk>/', DrinkViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='drink_detail'),
]
