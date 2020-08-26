from django.urls import path

from app.views import index, bus_stations, date_view

urlpatterns = [
    path('', index, name='index'),
    path('bus_stations/', bus_stations, name='bus_stations'),
    path('/<data>', date_view, name='date')
]
