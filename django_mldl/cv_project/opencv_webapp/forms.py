from django import forms
from .models import ImageUploadModel
'''
1) Hard-coded HTML: form, input, label, button, ...
2) forms.Form: 양식(Form class) 안에 받아들일 Field 선언
3) forms.ModelForm: Model class 안에 받아들일 Field를 선언하고 해당 클래스를 당겨와 활용
'''
class SimpleUploadForm(forms.Form):
    title = forms.CharField(max_length=50)
    image = forms.ImageField()

class ImageUploadForm(forms.ModelForm):
    # Form을 통해 받아들어야 할 데이터가 명시되어 있는 메타 데이터 (DB 테이블을 연결)
    class Meta:
        model = ImageUploadModel
        # Form을 통해 사용자로부터 입력 받으려는 Model Class의 field 리스트
        fields = ('description', 'document',) # uploaded_at
