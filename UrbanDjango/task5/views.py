from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

from task5.forms import UserRegister

users = ['user1', 'user2', 'user3', 'user4', 'user5']


# Create your views here.
def check_data(data):
    if data['username'] in users:
        return 'Пользователь уже существует'
    elif data['password'] != data['repeat_password']:
        return 'Пароли не совпадают'
    elif int(data['age']) < 18:
        return 'Вы должны быть старше 18'
    return f'Приветствуем, {data['username']}!'

def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            info = {'username': username,
                    'password': password,
                    'repeat_password': repeat_password,
                    'age': age,
                    }
            check = check_data(info)
            if 'Приветствуем' in check:
                info.update({'greetings': check})
            else:
                info.update({'error': check})
    else:
        form = UserRegister()
    info.update({'form': form})
    return render(request, 'registration_page.html', info)


def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        info = {'username': username,
                'password': password,
                'repeat_password': repeat_password,
                'age': age,
                }
        check = check_data(info)
        if 'Приветствуем' in check:
            info.update({'greetings': check})
        else:
            info.update({'error': check})
    return render(request, 'registration_page.html', info)
