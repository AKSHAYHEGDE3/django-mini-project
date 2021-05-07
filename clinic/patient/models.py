from django.db import models


# Create your models here.
class Patient(models.Model):
    patient_name=models.CharField(max_length=50)
    patient_mobile_no=models.CharField(max_length=10)
    patient_email=models.EmailField()
    # patient_appointment=models.DateField()