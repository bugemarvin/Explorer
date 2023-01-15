from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path("dashboard_users/", views.dashboard_users, name="index"),
    path("maps_users/", views.maps_users, name="maps"),
    path("inbox_users/", views.inbox_users, name="messages"),
    path("notification_users/", views.notification_users, name="notification"),
    path("settings_users/", views.settings_users, name="settings"),
    path("profile_users/", views.profile_users, name="settings"),
    path("login_users/", views.login_users, name="index"),
    path("logout_users/", views.logout_users, name="index"),
    path("signup_users/", views.signup_users, name="register"),
    path("reset_users/", views.resets_users, name="reset"),
    path("forgot_users/", views.forgot_users, name="forgot"),
]