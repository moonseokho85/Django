from django.contrib import admin
from polls.models import Question, Choice

# class ChoiceInline(admin.StackedInline):
#     model = Choice
#     extra = 2 # Default 로 보여줄 Choice 입력 slot 의 수

class ChoiceInline(admin.TabularInline): # TabularInline: 표 형식의 구조
    model = Choice
    extra = 2 # Default 로 보여줄 Choice 입력 slot 의 수

class QuestionAdmin(admin.ModelAdmin):
    # Question 추가 페이지 내 항목들의 순서 변경 지정
    # fields = ['pub_date', 'question_text'] # fields 변수명은 고정입니다

    # ('field 집합의 소제목 ', {'fields': ['field 이름 1', 'field 이름 2', ...]}),
    fieldsets = [
        ("Question title", {'fields': ['question_text']}),
        ("Date information", {'fields': ['pub_date'], 'classes': ['collapse']})
    ]

    inlines = [ChoiceInline]

    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date'] # pub_ 설문조사 생성 시간 을 기준으로 필터 기능 추가
    search_fields = ['question_text'] # question_ 설문조사 주제 를 기준으로 검색 기능 추가

# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
