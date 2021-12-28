from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('published-date')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now()-datetime.timedelta(days=1)


class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    vote_tally = models.IntegerField(default=0)
    associated_question = models.ForeignKey(Question,on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text
