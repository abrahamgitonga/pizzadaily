from django.db import models

# Create your models here.
class pizzaModel(models.Model):
    name = models.CharField(max_length=10)
    price = models.CharField(max_length=10)


class customerModel(models.Model):
    userid = models.CharField(max_length=10)
    telephone = models.CharField(max_length=10)

class orderModel(models.Model):
    username = models.CharField(max_length=10)
    telephone = models.CharField(max_length=10)
    address = models.CharField(max_length=10)
    ordereditems = models.CharField(max_length=10)   