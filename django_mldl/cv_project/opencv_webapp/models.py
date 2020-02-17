from django.db import models

# Create your models here.
class ImageUploadModel(models.Model):
    description = models.CharField(max_length=255, blank=True) # blank -> Optional
    # ses.jpg -> image/2020/02/17/ses.jpg
    document = models.ImageField(upload_to='image/%Y/%m/%d')
    # auto_now_add: 자동으로 저장되는 시점을 기준으로 현재 시간을 세팅
    uploaded_at = models.DateTimeField(auto_now_add=True)
