from django.shortcuts import render, get_object_or_404
from .models import *
from random import *
from datetime import datetime


# ------- Главная страница --------------------------------
def general(request):
    context = {
        "title": 'Главная',
        "head": 'Стартовая страница',
        "text": 'Сервер запущен и работает',
    }
    return render(request, "hw_app/general.html", context)


# ------- Тестовые данные ---------------------------------
def fake_datas(request):
    for i in range(5):
        user = User(
            name=f'Пользователь {i}',
            email=f'e{i}@mail.com',
            mobile=f'+7 (999) 555-44-0{i}',
            us_adrs=f'Регион, Город, Улица, Дом, Кв.',
        )
        user.save()
    for i in range(1, 21):
        product = Product(
            name=f'Товар - {i}',
            content=f'Описание товара ...',
            price=uniform(500, 10000),
            count=randint(1, 20),
        )
        product.save()
    for user in User.objects.all():
        order = Order(us_name=user)
        order.save()
        sum_price = 0
        l_pid = sample(list(i for i in range(1, 21)), 5)
        for pid in l_pid:
            order_product = Product.objects.filter(pk=pid).first()
            sum_price += order_product.price_get()
            order.products.add(order_product)
        order.sum_price = sum_price
        order.save()
    context = {
        "title": 'Data',
        "head": 'Fakes data',
        "text": 'Create fakes data is complete',
    }
    return render(request, "hw_app/general.html", context)


# ------- Список клентов ----------------------------------
def list_users(request):
    context = {"users": User.objects.all()}
    return render(request, "hw_app/dbu.html", context)


# ------- Список товаров ----------------------------------
def list_products(request):
    context = {"products": Product.objects.all()}
    return render(request, "hw_app/dbp.html", context)


# ------- Список заказов ----------------------------------
def list_orders(request):
    context = {"orders": Order.objects.all()}
    return render(request, "hw_app/dbo.html", context)


# ------- Список товаров в заказе -------------------------
def basket(request, uid):
    context = {
        'head': Order.objects.get(pk=uid).us_name,
        'basket': Order.objects.get(pk=uid).products.all(),
    }
    return render(request, "hw_app/dbbasket.html", context)


def us_products(request, uid):
    user = get_object_or_404(User, pk=uid)
    orders_list = Order.objects.filter(us_name=user)
    products_list = []
    for el in orders_list:
        products_list += Order.objects.get(pk=el.id).products.all()
    context = {'user_products': products_list} #.order_by('-id')[:5]
    return render(request, 'hw_app/us_prod.html', context)


def us_products_time(request, uid, dif_day):
    user = get_object_or_404(User, pk=uid)
    orders_list = Order.objects.filter(us_name=user)
    products_list = []
    for el in orders_list:
        delta = abs(el.order_day.replace(tzinfo=None) - datetime.utcnow())
        if delta.days < dif_day:
            products_list += Order.objects.get(pk=el.id).products.all()
    context = {'user_products': products_list}
    return render(request, 'hw_app/us_prod.html', context)
