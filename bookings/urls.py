from django.urls import path
from . import views

urlpatterns = [
    path("rooms/all/", views.all_rooms),
    path("seats/all/", views.all_seats),
    path("cars/all/", views.all_cars),
]

