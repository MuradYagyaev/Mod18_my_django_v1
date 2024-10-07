from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class Platform(TemplateView):
    template_name = 'platform.html'
    title = 'Мой магазин'
    h1_text = 'Главная страница'
    store_items = {
        '#': 'Главная',
        '/platform/games': 'Магазин',
        '/platform/cart': 'Корзина'
    }
    extra_context = {
        'title': title,
        'h1_text': h1_text,
        'store_items': store_items,
    }


class Games(TemplateView):
    template_name = 'games.html'
    title = 'Мой магазин'
    h1_text = 'Игры'
    games = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2', 'Doom 2']
    extra_context = {
        'title': title,
        'h1_text': h1_text,
        'games': games,
    }

class Cart(TemplateView):
    template_name = 'cart.html'
    title = 'Мой магазин'
    h1_text = 'Извините, ваша корзина пуста'
    extra_context = {
        'title': title,
        'h1_text': h1_text,
    }