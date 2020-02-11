from django.shortcuts import render
from django.http import HttpResponse # 추가됨
from lotto.models import GuessNumbers
from lotto.forms import PostForm
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
    lottos = GuessNumbers.objects.all()
    return render(request, 'lotto/default.html', {'lottos': lottos})

def hello(request):
    return HttpResponse("<h1 style='color:red;'>Hello, world!</h1>")

from .forms import PostForm

def post(request):
    form = PostForm()
    return render(request, "lotto/form.html", {"form": form})
