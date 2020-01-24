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
    payment = models.CharField( 
        max_length = 20, 
        choices = payment_choices, 
        default = 'IMEPay'
        ) 
    comment=models.TextField(null=True)
    def __str__(self):
        return self.name