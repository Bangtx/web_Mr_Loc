from django.db import models


# Create your models here.
class product(models.Model):
    name_product = models.CharField(max_length=100)
    link = models.CharField(max_length=1000)
    description = models.CharField(max_length=5000)
    cost = models.IntegerField(max_length=9)


class username(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=8)

