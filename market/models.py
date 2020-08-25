from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Product(models.Model):
    brand = models.CharField(max_length=50, null=False)
    model = models.CharField(max_length=75, null=False)
    price = models.FloatField(null=True)
    description = models.CharField(max_length=2000, null=True)
    catalogue = models.ForeignKey('Catalogue', on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return f'{self.brand} {self.model}'


class Catalogue(models.Model):
    name = models.CharField(max_length=75, null=False)

    def __str__(self):
        return self.name


class Order(models.Model):
    cart = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

