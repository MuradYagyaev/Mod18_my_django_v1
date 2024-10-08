"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from task2.views import func_temp, ClassTemp
from task3.views import Platform, Games, Cart
from task4.views import Platform2, Games2, Cart2
from task5.views import sign_up_by_django, sign_up_by_html


urlpatterns = [
    path('admin/', admin.site.urls),
    path('func/', func_temp),
    path('class/', ClassTemp.as_view()),
    path('platform/', Platform.as_view()),
    path('platform/games/', Games.as_view()),
    path('platform/cart/', Cart.as_view()),
    path('platform2/', Platform2.as_view()),
    path('platform2/games2/', Games2.as_view()),
    path('platform2/cart2/', Cart2.as_view()),
    path('django_sign_up/', sign_up_by_django),
    path('html_sign_up/', sign_up_by_html),
]
