from django.db import models

# Create your models here.

class Location(models.Model):
    location = models.CharField(max_length = 30)

    def __str__(self):
        return self.location

    def save_location(self):
        self.save()


class Category(models.Model):
    category = models.CharField(max_length = 30)

    def __str__(self):
        return self.category

    def save_category(self):
        self.save()


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

    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(category__category__icontains = search_term)
        return images

    def save_image(self):
        self.save()

    class Meta:
        ordering = ['image']



