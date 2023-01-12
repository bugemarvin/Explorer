from django.shortcuts import render

def index(request):
        return render(request, 'explorer/index.html', {})

def dashboard(request):
        return render(request, 'dashboard/index.html', {})

def maps(request):
        return render(request, 'dashboard/maps.html', {})

def messages(request):
        return render(request, 'dashboard/messages.html', {})

def notification(request):
        return render(request, 'dashboard/notification.html', {})

def settings(request):
        return render(request, 'dashboard/settings.html', {})

def login(request):
        return render(request, 'authentication/index.html', {})

def signup(request):
        return render(request, 'authentication/register.html', {})

def resets(request):
        return render(request, 'authentication/reset.html', {})

def forgot(request):
        return render(request, 'authentication/forgot.html', {})