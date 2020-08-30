from django.shortcuts import render
from django.http import HttpResponse
from market.models import Product


def main(request):
    template = 'home.html'
    products = Product.objects.filter()
    context = {'products': products}
    return render(request, template, context=context)

# Create your views here.
