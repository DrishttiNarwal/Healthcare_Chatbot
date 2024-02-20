from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "CareConnect/index.html")


def form(request):
    return render(request, 'form.html')


def chatbot(request):
    return render(request, 'chatbot.html')


def chatbot_view(request):
    return render(request, 'chatbot.html')


def form_view(request):
    # Add your form handling logic here if needed
    return render(request, 'form.html')


def brian(request):
    return HttpResponse("Hello, Brian!")


def david(request):
    return HttpResponse("Hello, David!")


# # views.py
# def greet(request):
#     # Get the value of 'name' parameter from the URL query string
#     name = request.GET.get('name', '')
#     return render(request, "CareConnect/greet.html", {
#         "name": name.capitalize()
#     })


def my_view(request):
    return render(request, 'image.html')
