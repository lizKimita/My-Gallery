from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length = 30)
    image_description = models.TextField()


class Location(models.Model):
    location = models.CharField(max_length = 30)


class Category(models.Model):
    category = models.CharField(max_length = 30)
