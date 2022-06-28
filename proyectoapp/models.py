from django.db import models

# Create your models here.
class Familia(models.Model):

    parentesco = models.CharField(max_length=30)
    nombre = models.CharField(max_length=15)
    edad = models.IntegerField()
    nacimiento = models.DateTimeField()
