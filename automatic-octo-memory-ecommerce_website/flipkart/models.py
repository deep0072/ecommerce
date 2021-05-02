from django.db import models

class Shoes(models.Model):
    name  =  models.CharField(max_length = 250)
    stock = models.IntegerField()
    price = models.FloatField()
    image = models.CharField(max_length = 2083)


class Electronics(models.Model):
    name  = models.CharField(max_length = 250)
    stock = models.IntegerField()
    Price = models.FloatField()
    image = models.CharField(max_length = 2043)


