from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def service(request):
    return render(request, 'service.html')


def team(request):
    return render(request, 'team.html')


def booking(request):
    return render(request, 'booking.html')


def menu(request):
    return render(request, 'menu.html')
