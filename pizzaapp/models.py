from django.db import models

# Create your models here.
class pizzaModel(models.Model):
    name = models.CharField(max_length=10)
    price = models.CharField(max_length=10)