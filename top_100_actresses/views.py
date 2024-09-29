from django.shortcuts import render
from django.views import View
from .models import Actresses
from .forms import ActressesForm
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.views.generic.edit import UpdateView, CreateView
from django.urls import reverse
from django.views.generic import DetailView

background_online = ['Смотреть онлайн', 'Фильмы', 'Сериалы', 'Каналы ТВ']

background_movies = [
    'Фильмы',
    'Расписание и билеты',
    'Фильмы онлайн',
    'Лучшие фильмы',
    'Подборки',
    'Календарь кинопремьер',
    'Премии',
    'Все фильмы',
]

background_serials = [
    'Сериалы',
    'Новинки',
    'Сериалы онлайн',
    'Сериалы онлайн',
    'Лучшие сериалы',
    'Подборки',
    'Календарь сериалов',
    'Телешоу',
    'Все сериалы',
]
background_tvshow = [
    'Телепрограммы',
    'Онлайн ТВ',
    'Избранные каналы',
    'Центральные каналы',
    'Местные каналы',
    'Спортивные каналы',
    'Детские каналы',
    'Все каналы',
    'Помощь',
]
background_stars = [
    'Интервью',
    'Красная дорожка',
    'Статьи',
    'Награды',
    'Сегодня родились',
]


class UpdateActressView(UpdateView):
    model = Actresses
    form_class = ActressesForm
    template_name = 'top_100_actresses/actress_form.html'
    success_url = 'done'


def done(request):
    return render(request, 'top_100_actresses/done_form.html')


class CreateActressView(CreateView):
    model = Actresses
    template_name = 'top_100_actresses/actress_form.html'
    fields = '__all__'
    success_url = 'done'


def show_all_actresses(request):
    actresses = Actresses.objects.all()
    data = {
        'actresses': actresses,
        'background_online': background_online,
        'background_movies': background_movies,
        'background_serials': background_serials,
        'background_tvshow': background_tvshow,
        'background_stars': background_stars,
    }
    return render(request, 'top_100_actresses/show_all_actresses.html', context=data)


class ActressDetailView(DetailView):
    template_name = 'top_100_actresses/show_one_actress.html'
    model = Actresses
    context_object_name = 'info'
