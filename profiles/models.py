from django.db import models
from django.core.validators import MaxLengthValidator

class PatientProfile(models.Model):
    GENDERS = [
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=GENDERS, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField(blank=True)
    phone_numeber = models.IntegerField(blank=True, null=True, validators=[MaxLengthValidator(10)])
    email = models.EmailField(max_length=255)

    def __str__(self):
        return f"{self.email}"
