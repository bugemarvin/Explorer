from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import 
from django.contrib import messages

def index(request):
        return render(request, 'explorer/index.html', {})

def dashboard_users(request):
        return render(request, 'dashboard/index.html', {})

def maps_users(request):
        return render(request, 'dashboard/maps.html', {})

def inbox_users(request):
        return render(request, 'dashboard/messages.html', {})

def notification_users(request):
        return render(request, 'dashboard/notification.html', {})

def settings_users(request):
        return render(request, 'dashboard/settings.html', {})


def profile_users(request):
        return render(request, 'dashboard/profile.html', {})

def login_users(request):
        if request.method == 'POST':
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                        login(request, user)
                        return render(request, 'dashboard/index.html', {})
                else:
                        messages.success(request, ('! Incorrect Username and Password'))
                        return render(request, 'authentication/index.html', {})
        else:
                return render(request, 'authentication/index.html', {})

def logout_users(request):
        logout(request)
        return render(request, 'explorer/index.html', {})

def signup_users(request):
        return render(request, 'authentication/register.html', {})

def resets_users(request):
        return render(request, 'authentication/reset.html', {})

def forgot_users(request):
        return render(request, 'authentication/forgot.html', {})