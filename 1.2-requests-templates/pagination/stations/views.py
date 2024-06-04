import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

STATIONS = {}
with open('data-398-2018-08-30.csv', mode='r', encoding='utf-8') as infile:
    csv_reader = csv.DictReader(infile)
    STATIONS = [row for row in csv_reader]


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    paginator = Paginator(STATIONS, 10)
    number_page = request.GET.get('page', 1)
    page = paginator.get_page(number_page)
    context = {
         'bus_stations': paginator.page(number_page),
         'page': page,
    }
    return render(request, 'stations/index.html', context)
