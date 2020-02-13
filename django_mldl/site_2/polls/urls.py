from django.urls import path
from . import views

urlpatterns = [
    # 127.0.0.1:8000/polls/" 이후의 URL 은 polls/urls.py 가 handling 하도록 만들 예정입니다
    path('', views.index, name='index'), # '127.0.0.1:8000/polls/' 를 받아내도록 만들어줄 것입니다

    # 127.0.0.1:8000/polls/3
    path('<int:question_id>/', views.detail, name='detail'),

    # 127.0.0.1:8000/polls/3/results
    path('<int:question_id>/results/', views.results, name='results'),

    # 127.0.0.1:8000/polls/3/vote
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
