from django.db import models
import datetime

# Create your models here.
class Patient(models.Model):
    patient_name=models.CharField(max_length=50)
    patient_mobile_no=models.CharField(max_length=10)
    patient_email=models.EmailField()
    patient_appointment=models.DateField(("Date"), default=datetime.date.today)

    def __str__(self):
        return self.patient_name
    