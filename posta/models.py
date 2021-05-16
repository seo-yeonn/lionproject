from django.db import models

# Create your models here.
class Bloga(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
