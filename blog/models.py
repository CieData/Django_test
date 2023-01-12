from django.db import models

# Create your models here.
class Post(models.Model):
    #데이터베이스의 컬럼 : 최대길이가 30
    title = models.CharField(max_length=30)
    content = models.TextField()

created_at = models.DateTimeField()