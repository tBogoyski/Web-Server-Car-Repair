from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    maker = models.CharField(max_length=100)
    year_of_make = models.DateField()
    registration_number = models.CharField(max_length=8)


class Event(models.Model):
    date_of_event = models.DateTimeField()
    km_of_car = models.IntegerField()
    event_text = models.TextField()
    periodic_event = models.BooleanField()
    next_date = models.DateField()
    next_change = models.DateField()
