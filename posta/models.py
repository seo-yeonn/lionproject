from django.db import models

# Create your models here.
class Bloga(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    image = models.ImageField(upload_to="post_img/", blank=True,null=True)
    def __str__(self):
        return self.name
