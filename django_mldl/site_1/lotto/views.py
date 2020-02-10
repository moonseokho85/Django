from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    sample_str = 'Hi this is python str'
    return render(request, 'lotto/index.html', {'main_str': sample_str})

def hello(request):
    return HttpResponse("<h1 style='color:red;'>Hello, world!</h1>")
