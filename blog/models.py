from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)  #CharField는 짧은 형식
    pub_date = models.DateTimeField('data published') #날짜와 시간
    body = models.TextField() #TextField는 긴 형식
    
#자기자신의 타이틀을 내보내는 코드
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]