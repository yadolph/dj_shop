from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    orders = models.ManyToManyField('Order', related_name='user_of_order')


class Product(models.Model):
    brand = models.CharField(max_length=50, null=False)
    model = models.CharField(max_length=75, null=False)
    price = models.FloatField(null=True)
    description = models.CharField(max_length=2000, null=True)
    catalogue = models.ForeignKey('Catalogue', on_delete=models.CASCADE, related_name='products_of_catalogue')


class Catalogue(models.Model):
    name = models.CharField(max_length=75, null=False)
    products = models.ManyToManyField('Product', related_name='catalogue_of_product')


class Order(models.Model):
    cart = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders_of_user')


class OrderForUser(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class ProductToCatalogue(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    catalogue = models.ForeignKey(Catalogue, on_delete=models.CASCADE)
# Create your models here.
