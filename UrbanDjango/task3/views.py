from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class Platform(TemplateView):
    template_name = 'platform.html'
    title = 'Мой магазин'
    pagename = 'Главная страница'
    store_items = {
        '#': 'Главная',
        '/platform/games': 'Магазин',
        '/platform/cart': 'Корзина'
    }
    extra_context = {
        'title': title,
        'pagename': pagename,
        'store_items': store_items,
    }


class Games(TemplateView):
    template_name = 'games.html'
    title = 'Мой магазин'
    pagename = 'Игры'
    games = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2', 'Doom 2']
    extra_context = {
        'title': title,
        'pagename': pagename,
        'games': games,
    }


class Cart(TemplateView):
    template_name = 'cart.html'
    title = 'Мой магазин'
    pagename = 'Извините, ваша корзина пуста'
    extra_context = {
        'title': title,
        'pagename': pagename,
    }
