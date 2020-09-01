from django.db import models
from django.contrib.auth.models import AbstractUser
import json
from ckeditor.fields import RichTextField


class User(AbstractUser):
    pass


class Product(models.Model):
    brand = models.CharField(max_length=50, null=False)
    model = models.CharField(max_length=75, null=False)
    price = models.FloatField(null=True)
    brief = models.CharField(max_length=500, null=True)
    description = models.CharField(max_length=5000, null=True)
    catalogue = models.ForeignKey('Catalogue', on_delete=models.CASCADE, related_name='products')
    picture = models.ImageField(upload_to='pics/%Y/%m/%d', default='pics/nopic.jpg')


    def __str__(self):
        return f'{self.brand} {self.model}'


class Article(models.Model):
    name = models.CharField(max_length= 75, null=False)
    brief = models.CharField(max_length=500, null=False, default='Краткое описание статьи')
    picture = models.ImageField(upload_to='pics/%Y/%m/%d', default='pics/nopic.jpg')
    text = models.CharField(max_length=15000, null=False)
    products = models.ManyToManyField(Product, related_name='articles')

    def __str__(self):
        return self.name


class Catalogue(models.Model):
    name = models.CharField(max_length=75, null=False)

    def __str__(self):
        return self.name


class Order(models.Model):
    cart = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def create_cart(self, cart):
        self.cart = json.dumps(cart)

    def load_cart(self):
        return json.load(self.cart)

