from django.db import models

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=90)
    body = models.CharField(max_length=1000)
    def __str__(self):
        return self.email

class Booking(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    members = models.IntegerField()
    email = models.EmailField()
    date = models.DateField()
    time = models.CharField(max_length=20)
    message = models.CharField(max_length=1000)
    def __str__(self):
        return self.email
