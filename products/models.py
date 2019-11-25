from django.db import models


# models.Model inheritance relationship is from django
# which will have base capability added like compatible with database etc.


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)  # 2083 is standard for url.


class Offer(models.Model):
    code = models.CharField(max_length=255)
    description = models.CharField(max_length=2083)
    discount = models.FloatField()
