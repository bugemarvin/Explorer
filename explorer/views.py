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