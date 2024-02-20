from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "CareConnect/index.html")


def form(request):
    return render(request, 'form.html')


def form_view(request):
    # Add your form handling logic here if needed
    return render(request, 'form.html')


def brian(request):
    return HttpResponse("Hello, Brian!")


def david(request):
    return HttpResponse("Hello, David!")


def greet(request, name):
    return render(request, "CareConnect/greet.html", {
        "name": name.capitalize()
    })


def my_view(request):
    return render(request, 'image.html')
