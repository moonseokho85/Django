from django.shortcuts import render
from django.http import HttpResponse # 추가됨
# Create your views here.

def index(request):
    '''
    site_1\lotto\templates\default.html (X) -> site_1\lotto\templates\lotto\default.html (O)

    site_1\member\templates\index.html (127.0.0.1:8000/member/)
    site_1\products\templates\index.html (127.0.0.1:8000/products)
    site_1\history\templates\index.html (127.0.0.1:8000/history)

    templates\index.html, index.html, index.html (X)

    site_1\member\templates\member\index.html (127.0.0.1:8000/member/)
    site_1\products\templates\products\index.html (127.0.0.1:8000/products)
    site_1\history\templates\history\index.html (127.0.0.1:8000/history)

    templates\ member\index.html, products\index.html, history\index.html (O)
    '''
    sample_str = "This is python variable"
    return render(request, 'lotto/default.html', {'pass_str': sample_str})

def hello(request):
    return HttpResponse("<h1 style='color:red;'>Hello, world!</h1>")
