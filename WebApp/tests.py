from django.test import TestCase
from .models import Book,Guest,Room,Hotel
from django.contrib.auth.models import User


# Create your tests here.
class ModelTestCase(TestCase):

    def setUp(self):
        guest1 = Guest.objects.create(name="Shakti",email="shaktiyakhha@gmail.com",phone=9810138740)
    
    def test_valid_guest(self):
        guest2 = Guest.objects.get(name="Shakti")
        value=guest2.is_valid_guest()
        self.assertTrue(value,True)
    
