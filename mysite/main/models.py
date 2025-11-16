from django.db import models

class Articles(models.Model):
    title = models.CharField('Название', max_length=100)
    anons = models.CharField('Анонс', max_length=500)
    FULL = models.TextField('Статья')
    date = models.DateField('Дата')
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f"/news/{self.id}"
# Create your models here.
