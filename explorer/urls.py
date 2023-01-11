from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path("dashboard/", views.dashboard, name="index"),
    path("maps/", views.maps, name="index"),
    path("messages/", views.messages, name="index"),
    path("notification/", views.notification, name="index"),
    path("settings/", views.settings, name="index"),
]