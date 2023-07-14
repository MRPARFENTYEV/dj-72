from django.http import HttpResponse
from django.shortcuts import render, reverse
import os
from datetime import datetime


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.now()
    # return current_time
    # current_time = None
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


# def workdir_view(request):
#     path = '.'
#     rez = sorted(os.listdir(path))
#     for n, item in enumerate(rez):
#         output = n + 1, item
#         return HttpResponse(workdir_view())
# raise NotImplemented


def workdir_view(request):
    path = '.'
    rez = [os.listdir(path)]
    return HttpResponse(rez)
    # raise NotImplemented







# Create your views here.
