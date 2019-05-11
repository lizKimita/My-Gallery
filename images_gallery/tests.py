from django.test import TestCase
from .models import Image, Location, Category

# Create your tests here.
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
