from django.db import models

class questionBank(models.Model):
    ques=models.TextField(default="sample question")
    marks=models.IntegerField(default=0)
    chapter_number=models.IntegerField(default=0)
    subj=models.CharField(max_length=20,default="CSE")
# Create your models here.
