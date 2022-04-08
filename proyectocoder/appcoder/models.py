from django.db import models

# Create your models here.


class Padres(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    ci = models.IntegerField(primary_key=True)

class Hijos(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    ci = models.IntegerField(primary_key=True)