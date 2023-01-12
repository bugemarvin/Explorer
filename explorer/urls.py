from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path("dashboard/", views.dashboard, name="index"),
    path("maps/", views.maps, name="maps"),
    path("messages/", views.messages, name="messages"),
    path("notification/", views.notification, name="notification"),
    path("settings/", views.settings, name="settings"),
    path("login/", views.login, name="index"),
    path("signup/", views.signup, name="register"),
    path("reset/", views.resets, name="reset"),
    path("forgot/", views.forgot, name="forgot"),
] 