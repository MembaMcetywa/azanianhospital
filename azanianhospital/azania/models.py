from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#models will consist of 3 entitites: patients, doctors, bookings
class patient(models.Model):
    patient_name = models.CharField(max_length =100)
    patient_lastname = models.CharField(max_length = 100)

    def __str__(self):
        return self.patient_name

class doctor(models.Model):
    doctor_name = models.CharField(max_length=100)
    doctor_lastname = models.CharField(max_length=100)
    def __str__(self):
        return self.doctor_name


class appointments(models.Model):
    patient_name = models.CharField(max_length=100)
    doctor_name = models.CharField(max_length=100)
    date = models.DateTimeField()
    def __str__(self):
        return self.patient_name
