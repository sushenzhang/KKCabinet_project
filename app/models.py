"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Pic(models.Model):
    material = models.ForeignKey('Material',on_delete = models.CASCADE)
    color = models.ForeignKey('Color',on_delete = models.CASCADE)
    object = models.ForeignKey('Object',on_delete = models.CASCADE)
    image = models.ImageField(default='.\static\app\images\1318967_1.jpg')

class Material(models.Model):
    wood = models.BooleanField(default=False)
    stone = models.BooleanField(default=False)

class Color(models.Model):
    white = models.BooleanField(default=False)
    grey = models.BooleanField(default=False)
    black = models.BooleanField(default=False)
    brown = models.BooleanField(default=False)

class Object(models.Model):
    kitchen = models.BooleanField(default=False)
    countertop = models.BooleanField(default=False)
    tv = models.BooleanField(default=False)
