from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name


class Extra(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    extra_name = models.CharField(max_length=255)
    extra_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.extra_name


class Drink(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    drink_name = models.CharField(max_length=255)
    drink_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.drink_name
