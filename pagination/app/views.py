from pprint import pprint

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv
new_file = None
with open('data-398-2018-08-30.csv', 'r', encoding='cp1251') as file:
    file_with_content = csv.DictReader(file, delimiter=',')
    new_file = list(file_with_content)


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    paginator = Paginator(new_file, 10)
    current_page = int(request.GET.get('page', 1))
    page_obj = paginator.get_page(current_page)
    if page_obj.has_next():
        next_page_url = page_obj.next_page_number()
    msg = page_obj.object_list
    pprint(msg)
    return render(request, 'index.html', context={
        'bus_stations': msg,
        'current_page': current_page,
        'prev_page_url': None,
        'next_page_url': next_page_url,
    })


def date_view():
    pass
