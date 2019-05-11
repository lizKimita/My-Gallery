from django.test import TestCase
from .models import Image, Location, Category

# Create your tests here.
class LocationTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.kenya = Location(location = "kenya")

     # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.kenya,Location))

        # Testing Save method
    def test_save_method(self):
        self.kenya.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)


class CategoryTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.nature = Category(category = "nature")

     # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.nature,Category))

        # Testing Save method
    def test_save_method(self):
        self.nature.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)>0)

class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        # Location class test
        self.kenya = Location(location = "kenya")

        # Category class Test
        self.nature = Category(category = "nature")

        # Image class Test
        self.image = Image(image = "",name="nature goodness", description = "I love this view", pub_date = "10/2/2019", location = self.kenya, category = self.nature)

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))

    # Testing Save method
    def test_save_method(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)