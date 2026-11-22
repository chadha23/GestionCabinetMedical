from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, RegexValidator


class Specialite(models.Model):
    nom_specialite = models.CharField(max_length=100)

    def __str__(self):
        return self.nom_specialite


class Medecin(User):
    matricule_ordre = models.CharField(
        max_length=6,
        primary_key=True,
        validators=[MinLengthValidator(6)]
    )

    telephone = models.CharField(
        max_length=8,
        validators=[RegexValidator(r'^\d{8}$')]
    )

    specialites = models.ManyToManyField(Specialite)

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name}"
