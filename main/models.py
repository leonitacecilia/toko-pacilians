from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.IntegerField()
    description = models.TextField()
    nutrition = models.CharField(max_length=300)
    sweetness = models.IntegerField()