from django.test import TestCase
from .models import Book,Guest,Room,Hotel
from django.contrib.auth.models import User


# Create your tests here.
class ModelTestCase(TestCase):

    def setUp(self):
        guest1 = Guest.objects.create(name="Shakti",email="shaktiyakhha@gmail.com",phone=9810138740)
        book1  = Book.objects.create(name="Bigyan",email="gyan@gamil.com",phone=9874552111,number_of_adults=1,number_of_children=2,arrival="2016-02-25",checkOut="2018-03-25")

    
    def test_valid_guest(self):
        guest2 = Guest.objects.get(name="Shakti")
        value=guest2.is_valid_guest()
        self.assertTrue(value,True)
    
    def test_guest_name(self):
        guest3=Guest.objects.get(name="Shakti")
        self.assertEqual(guest3.name,'Bigyan')

    def test_book_name(self):
        books=Book.objects.get(name="Bigyan")
        self.assertEqual(books.name,"Bigyan")
    
    def test_valid_phone(self):
        book2=Book.objects.get(phone="9874552111")
        value=book2.is_valid_phone()
        self.assertFalse(value,True)

    def test_valid_book(self):
        b = Book.objects.get(arrival="2016-02-25",checkOut="2018-03-25")
        value=b.is_valid_book()
        self.assertTrue(b,True)
    
    
