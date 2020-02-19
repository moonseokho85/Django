from django.urls import path
from countdown import views

app_name = 'countdown'

urlpatterns = [
    path('', views.index, name='index')
]
