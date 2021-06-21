from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    generation = models.CharField(max_length=50)
    major = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)
    age = models.CharField(max_length=50)