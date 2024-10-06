from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class Platform(TemplateView):
    template_name = 'platform.html'
    store_items = ['Главная', 'Магазин', 'Корзина']
    context = {
        'title': 'Игры',
        'h1_title': 'Главная страница',
        'store_items': store_items,
    }


class Games(TemplateView):
    template_name = 'games.html'


class Cart(TemplateView):
    template_name = 'cart.html'
