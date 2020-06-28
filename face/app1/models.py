from django.db import models

# Create your models here.

class dataBase(models.Model):


    selected = models.FloatField(default=0)
    voted = models.FloatField(default=0)
    votePer = models.FloatField(default=0)

