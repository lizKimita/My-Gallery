from django.db import models

# Create your models here.

class Location(models.Model):
    location = models.CharField(max_length = 30)

    def __str__(self):
        return self.location


class Category(models.Model):
    category = models.CharField(max_length = 30)

    def __str__(self):
        return self.category


class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length = 30)
    description = models.TextField(max_length = 60)
    pub_date = models.DateTimeField(auto_now_add = True)
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)


    @classmethod
    def get_images(cls):
        image = cls.objects.all()
        return image

    class Meta:
        ordering = ['image']



