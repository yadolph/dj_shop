from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, logout, login
from django.db import IntegrityError

from market.models import Product, Article, Catalogue, User, Order
from market.forms import RegUser, LoginUser, AddToCart, ModifyCartForm

import json
from random import randint


def auth_check(request):
    user = request.user
    if user.is_authenticated:
        auth = True
    else:
        auth = False
    context = {'auth': auth, 'username': user.username}
    return context


def home(request):
    template = 'home.html'
    articles = Article.objects.filter()
    username = request.user
    if request.user.is_anonymous:
        username = 'Гость'

    featured_products = []
    pulled_products = Product.objects.all().order_by('-id')[:10]
    while len(featured_products) < 3:
        product_to_feature = pulled_products[randint(0,len(pulled_products)-1)]
        if product_to_feature not in featured_products:
            featured_products.append(product_to_feature)

    context = {'articles': articles, 'username': username, 'featured_products': featured_products}
    context.update(auth_check(request))
    return render(request, template, context=context)


def article_full(request, pk):
    template = 'article_full.html'
    article = get_object_or_404(Article, id=pk)
    featured_products = article.products.all()
    context = {'article': article, 'featured_products': featured_products}
    context.update(auth_check(request))
    return render(request, template, context=context)
    pass


def product_full(request, pk):
    cart = request.session.get('cart', {})
    prod_id = str(pk)
    template = 'product_full.html'
    product = get_object_or_404(Product, id=pk)
    form = AddToCart()
    result = ''

    if request.method == 'POST':
        if not prod_id in cart.keys():
            quantity = int(request.POST.get('quantity'))
            cart[prod_id] = quantity
            request.session['cart'] = cart
            result = 'success'
        else:
            result = 'failure'
    context = {'product': product, 'form': form, 'result': result}
    context.update(auth_check(request))
    return render(request, template, context=context)


def catalogue_main(request):
    template = 'cat.html'
    catalogues = Catalogue.objects.filter()
    context = {'catalogues': catalogues}
    context.update(auth_check(request))
    return render(request, template, context=context)


def catalogue_section(request, pk):
    template = 'cat_section.html'
    catalogue = get_object_or_404(Catalogue, id=pk)
    products = catalogue.products.all()
    context = {'catalogue': catalogue, 'products': products}
    context.update(auth_check(request))
    return render(request, template, context=context)


def signup(request):
    result = ''
    form = RegUser()

    if request.method == 'POST':
        username = request.POST.get('email')
        email = username
        password = request.POST.get('password')
        password_check = request.POST.get('password_check')

        if password != password_check:
            return render(request, 'signup.html', {'result': 'Пароли не совпадают', 'form': form})

        try:
            new_user = User.objects.create_user(username, email=email, password=password)
        except IntegrityError:
            return render(request, 'signup.html', {'result': 'Такой пользователь уже существует', 'form': form})

        result = f'Пользователь {new_user.username} создан'

    return render(
        request,
        'signup.html',
        {'form': form, 'result': result}
    )


def login_user(request):
    result = ''
    form = LoginUser()

    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            result = 'Вы успешно вошли в систему'
        else:
            result = 'Ошибка. Проверьте введенные данные'

    return render(
        request,
        'login.html',
        {'form': form, 'result': result}
    )


def logout_user(request):
    logout(request)

    return render(
        request,
        'logout.html',
    )

def cart(request):
    if request.method == 'POST':
        id = request.POST.get('product_id')
        quantity = request.POST.get('quantity')
        if int(quantity) <= 0:
            del request.session['cart'][str(id)]
            request.session.modified = True
        else:
            request.session['cart'][str(id)] = int(quantity)
            request.session.modified = True

    template = 'cart.html'
    cart_list = []
    cart = request.session.get('cart', '')
    form = ModifyCartForm()
    if cart:
        for key, val in cart.items():
            products = (get_object_or_404(Product, id=int(key)), val)
            cart_list.append(products)
    context = {'cart_list': cart_list, 'form': form}
    context.update(auth_check(request))
    return render(request, template, context=context)

def order(request):
    template = 'orders.html'
    if request.method == 'POST':
        cart = request.session.get('cart')
        cart = json.dumps(cart)
        user = request.user
        new_order = Order(cart=cart, user=user)
        new_order.make_pretty_cart()
        new_order.save()
        request.session['cart'].clear()
        request.session.modified = True
        context = {'orders': ''}
        context.update(auth_check(request))
        return render(request, template, context)
    else:
        user = request.user
        orders = Order.objects.filter(user=user).all()
        context = {'orders': orders}
        context.update(auth_check(request))
        return render(request, template, context)
