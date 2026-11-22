from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils import timezone


class Patient(User):
    cin = models.CharField(
        max_length=8,
        primary_key=True,
        validators=[RegexValidator(r'^\d{8}$')]
    )

    telephone = models.CharField(
        max_length=8,
        validators=[RegexValidator(r'^\d{8}$')]
    )

    date_naissance = models.DateField()

    def clean(self):
        super().clean()

        if self.date_naissance and self.date_naissance >= timezone.localdate():
            raise ValidationError({
                'date_naissance': "La date de naissance doit être antérieure à aujourd'hui."
            })

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
