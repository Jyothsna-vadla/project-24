from django.db import models
from app.models import *

# Create your models here.
class school(models.Model):
    sname=models.CharField(max_length=100,primary_key=True)
    slocation=models.CharField(max_length=100)
    sprincipal=models.CharField(max_length=100)
    def __str__(self):
        return self.sname
