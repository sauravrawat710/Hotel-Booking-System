from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Hotel(models.Model):
    status = (
        ('Available', 'Available'),
        ('Not Available', 'Not Available')
    )
    name = models.CharField(max_length=100)
    desc = models.TextField()
    status = models.CharField(max_length=100, choices=status)
    price = models.PositiveIntegerField(default=0)
    image = models.ImageField(default='default.jpg', upload_to='hotel_pic')

    def __str__(self):
        return self.name


class Booking(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    guest = models.ForeignKey(User, on_delete=models.CASCADE)
    no_of_guest = models.PositiveIntegerField(default=0)
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f"{self.hotel}'s booking"
    