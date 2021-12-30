from django.urls import path
from . import views



urlpatterns = [
    path('flightstauts/',views.get_flight_board,name='flight_board'),
]
