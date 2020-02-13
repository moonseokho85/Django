from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Question(models.Model): # DB Table for 설문조사 주제
    question_text = models.CharField(max_length=200) # 설문조사 주제 텍스트
    pub_date = models.DateTimeField('date published') # ‘date published’ : 관리자 페이지에서 보여질 항목명

    def __str__(self): # Admin page 에서 display 되는 텍스트에 대한 변경
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now >= self.pub_date >= now - datetime.timedelta(days=1)

    # 관리자 페이지 Question 리스트에서 True/False 문구를 아이콘으로 변경
    was_published_recently.boolean = True

    # 'WAS PUBLISHED RECENTLY' 열의 정렬 기준을 pub_date( 설문조사 주제 생성 시간 로 세팅
    was_published_recently.admin_order_field = 'pub_date'

    # 'WAS PUBLISHED RECENTLY' 열의 이름 변경
    was_published_recently.short_description = 'Published recently?'
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # 설문조사 주제의 id 값
    choice_text = models.CharField(max_length=200) # 설문조사 주제에 대한 선택지 텍스트
    votes = models.IntegerField(default=0) # 해당 선택지의 득표 수

    def __str__(self): # Admin page 에서 display 되는 텍스트에 대한 변경
        return self.choice_text
