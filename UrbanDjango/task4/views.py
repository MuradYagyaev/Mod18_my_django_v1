from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class Platform2(TemplateView):
    template_name = 'platform2.html'
    title = 'Главная'
    pagename = 'Главная страница'
    store_items = {
        '#': 'Главная',
        '/platform2/games2': 'Магазин',
        '/platform2/cart2': 'Корзина'
    }
    extra_context = {
        'title': title,
        'pagename': pagename,
        'store_items': store_items,
    }


class Games2(TemplateView):
    template_name = 'games2.html'
    title = 'Каталог'
    pagename = 'Игры'
    games = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2', 'Doom 2']
    extra_context = {
        'title': title,
        'pagename': pagename,
        'games': games,
    }


class Cart2(TemplateView):
    template_name = 'cart2.html'
    title = 'Корзина'
    pagename = 'Корзина'
    content = 'Извините, ваша корзина пуста'
    extra_context = {
        'title': title,
        'pagename': pagename,
        'content': content,
    }
