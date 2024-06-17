from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(
        validators=[MaxValueValidator(999999), MinValueValidator(-999999)]
    )
    booking_date = models.DateTimeField()
    
    def get_item(self):
        return f'{self.name} : {str(self.booking_date)}'
    
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(
        validators=[MaxValueValidator(99999), MinValueValidator(-99999)]
    )
    def get_item(self):
        return f'{self.title} : {str(self.price)}'  