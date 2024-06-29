from django.db import models
from django.core.validators import MaxLengthValidator, RegexValidator


class PatientProfile(models.Model):
    GENDERS = [
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=GENDERS, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField(blank=True)
    phone_number = models.CharField(max_length=12, blank=True, null=True)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return f"{self.email}"
