from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()


    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100] #바디라고 지정한 글 부분을 100개로 제한한다.