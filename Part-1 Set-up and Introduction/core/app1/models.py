from django.db import models


class Animal(models.Model):
    name = models.CharField(max_length=50)
    sound = models.CharField(max_length=50)