from django.db import models


# specifying choices 
  
payment_choices = ( 
    ("IMEPay","IMEPay"), 
    ("Khalti","Khalti"), 
    ("IPay","IPay"), 
    ("Prabhu Pay","Prabhu Pay"), 
    ("E-sewa","E-sewa"),    
)

# Create your models here.

class Book(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(null=True, max_length=50)
    phone=models.IntegerField()
    number_of_adults=models.IntegerField()
    number_of_children=models.IntegerField()
    arrival=models.DateField()
    checkOut=models.DateField()




class Guest(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(null=True, max_length=50)
    phone=models.IntegerField()

    def __str__(self):
        return f"the guest in {self.Hotel}"

class Room(models.Model):
    number=models.IntegerField()
    level=models.IntegerField()
    types=models.CharField(max_length=20)
    guests = models.ForeignKey(Guest,on_delete = models.CASCADE)
    booking = models.ManyToManyField(Book) # booking may of many rooms at the same time one room may have multiple bookings


    def __str__(self):
        return f"the  {self.Hotel}contains room"




class Hotel(models.Model):
    hotel_name = models.CharField(max_length = 50)
    place = models.CharField(max_length = 50)
    guests = models.ManyToManyField(Guest)
    payment = models.CharField( 
        max_length = 20, 
        choices = payment_choices, 
        default = 'IMEPay'
        ) 
    comment=models.TextField(null=True)
    room = models.ForeignKey(Room,on_delete = models.CASCADE)
    def __str__(self):
        return self.name

