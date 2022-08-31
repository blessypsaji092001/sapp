from django.db import models

class Emp(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    salary=models.PositiveIntegerField()
    experience=models.CharField(max_length=50)

# Create your models here.
