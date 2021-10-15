from django.db import models
from django.utils import timezone
from datetime import timedelta

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published') #nome para visualização
    created = models.DateTimeField(auto_now_add =True)
    updated = models.DateTimeField(auto_now =True)

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now()-datetime.timedelta(days=1)
        
class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text    
