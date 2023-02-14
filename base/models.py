from django.db import models

# Create your models here.


class Employee(models.Model):
    Empcode = models.CharField(max_length=10, unique=True)
    firstName = models.CharField(max_length=150, null=True)
    middleName = models.CharField(max_length=100, null=True)
    lastName = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=30, null=True, unique=True)
    phoneNo = models.CharField(max_length=12, null=True, unique=True)
    address = models.CharField(max_length=500, default='record not available', null=True)
    DOB = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=5, null=True)
    qualification = models.CharField(max_length=50, null=True)
    salary = models.FloatField(max_length=50, null=True)

    def __str__(self):
        return self.firstName

    objects = models.Manager()
