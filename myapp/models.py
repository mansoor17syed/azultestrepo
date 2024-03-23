from django.db import models
from datetime import datetime


class Patient(models.Model):
    patient_name = models.CharField(max_length=255)
    blood_group = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.patient_name} - {self.blood_group}"
    


class Student(models.Model):

    student_name = models.CharField(max_length = 120)
    student_age = models.IntegerField()
    student_marks = models.IntegerField()    
    



class currencydata(models.Model):

    country_name = models.CharField(max_length = 120)
    country_code = models.CharField(max_length=5)
    country_currency_value = models.DecimalField(max_digits=25, decimal_places=20)
    currency_update_time = models.DateTimeField(default=datetime.now, blank=True)