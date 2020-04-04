"""
Definition of models.
"""

from django.db import models

# Create your models here.

class Material(models.Model):
    material = models.CharField(max_length = 50,default = 'N/A')
    def __str__(self):
        return self.material

class Color(models.Model):
    color = models.CharField(max_length = 50,default = 'N/A')
    def __str__(self):
        return self.color

class Classify(models.Model):
    classify = models.CharField(max_length = 200,default = 'N/A')
    def __str__(self):
        return self.classify

class Pic(models.Model):
    material = models.ManyToManyField(Material,blank=True)
    color = models.ManyToManyField(Color,blank=True)
    classify = models.ManyToManyField(Classify,blank=True)
    image = models.ImageField(upload_to = "gallery",default=None)
    is_on_home_page = models.BooleanField(default = False)
    is_on_home_page_gallery = models.BooleanField(default = False)
    def __str__(self):
        return self.image.name
