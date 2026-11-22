from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from django.utils import timezone

from Medecin.models import Medecin
from Patient.models import Patient


class RendezVous(models.Model):

    class Statut(models.TextChoices):
        EN_ATTENTE = 'EN_ATTENTE', 'En attente'
        CONFIRME = 'CONFIRME', 'Confirmé'
        ANNULE = 'ANNULE', 'Annulé'

    medecin = models.ForeignKey(
        Medecin,
        on_delete=models.CASCADE
    )

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE
    )

    motif = models.TextField()

    ordonnance = models.FileField(
        upload_to='ordonnances/',
        blank=True,
        validators=[FileExtensionValidator(['pdf'])]
    )

    statut = models.CharField(
        max_length=20,
        choices=Statut.choices,
        default=Statut.EN_ATTENTE
    )

    duree_minutes = models.PositiveIntegerField(default=30)

    date_rdv = models.DateTimeField()

    date_creation = models.DateTimeField(auto_now_add=True)

    date_maj = models.DateTimeField(auto_now=True)

    def clean(self):
        super().clean()

        if self.date_rdv:
            date_modifiee = True

            if self.pk is not None:
                ancienne_date = (
                    type(self).objects
                    .filter(pk=self.pk)
                    .values_list('date_rdv', flat=True)
                    .first()
                )
                date_modifiee = ancienne_date != self.date_rdv

            if date_modifiee and self.date_rdv <= timezone.now():
                raise ValidationError({
                    'date_rdv': "La date du rendez-vous doit être future."
                })

    class Meta:
        ordering = ['date_rdv']
        constraints = [
            models.UniqueConstraint(
                fields=['medecin', 'date_rdv'],
                name='unique_medecin_date_rdv'
            )
        ]

    def __str__(self):
        return f"RDV - {self.patient} avec {self.medecin} le {self.date_rdv}"
