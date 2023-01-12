from django.db import models
class Post(models.Model):
    #	데이터베이스의 필드(컬럼): 최대 길이가 30
    title	=	models.CharField(max_length=30)	
    content	=	models.TextField()
    created_at =	models.DateTimeField()
    #	author는 추후 작성