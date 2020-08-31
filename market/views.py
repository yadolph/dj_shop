from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from market.models import Product, Article, Catalogue


def home(request):
    template = 'home.html'
    articles = Article.objects.filter()
    context = {'articles': articles}
    return render(request, template, context=context)


def article_full(request, pk):
    template = 'article_full.html'
    article = get_object_or_404(Article, id=pk)
    featured_products = article.products.all()
    context = {'article': article, 'featured_products': featured_products}
    return render(request, template, context=context)
    pass


def product_full(request, pk):
    template = 'product_full.html'
    product = get_object_or_404(Product, id=pk)
    context = {'product': product}
    return render(request, template, context=context)


def catalogue_main(request):
    template = 'cat.html'
    catalogues = Catalogue.objects.filter()
    context = {'catalogues': catalogues}
    return render(request, template, context=context)

def catalogue_section(request, pk):
    template = 'cat_section.html'
    catalogue = get_object_or_404(Catalogue, id=pk)
    products = catalogue.products.all()
    context = {'catalogue': catalogue, 'products': products}
    return render(request, template, context=context)

# Create your views here.
