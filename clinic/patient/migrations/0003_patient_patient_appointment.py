# Generated by Django 3.1.7 on 2021-05-08 11:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_remove_patient_patient_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='patient_appointment',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]