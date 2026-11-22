from datetime import timedelta

from django.contrib import admin
from django.db.models import Sum
from django.utils import timezone

from .models import RendezVous


class DateRendezVousFilter(admin.SimpleListFilter):
    title = "Date du rendez-vous"
    parameter_name = "periode"

    def lookups(self, request, model_admin):
        return (
            ("aujourdhui", "Aujourd'hui"),
            ("semaine", "Cette semaine"),
            ("avenir", "À venir"),
        )

    def queryset(self, request, queryset):
        aujourd_hui = timezone.localdate()

        if self.value() == "aujourdhui":
            return queryset.filter(date_rdv__date=aujourd_hui)

        if self.value() == "semaine":
            debut = aujourd_hui - timedelta(days=aujourd_hui.weekday())
            fin = debut + timedelta(days=7)

            return queryset.filter(
                date_rdv__date__gte=debut,
                date_rdv__date__lt=fin
            )

        if self.value() == "avenir":
            return queryset.filter(date_rdv__gt=timezone.now())

        return queryset


@admin.register(RendezVous)
class RendezVousAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "medecin",
        "patient",
        "date_rdv",
        "statut",
        "duree_minutes",
        "duree_confirmee_aujourdhui",
    )

    list_filter = (
        "statut",
        "medecin",
        DateRendezVousFilter,
    )

    list_per_page = 10

    autocomplete_fields = ["medecin", "patient"]

    readonly_fields = ["date_creation", "date_maj"]

    fieldsets = (
        ("Participants", {
            "fields": ("medecin", "patient"),
        }),
        ("Planification", {
            "fields": ("date_rdv", "duree_minutes", "statut"),
        }),
        ("Dossier", {
            "fields": ("motif", "ordonnance"),
        }),
        ("Suivi", {
            "fields": ("date_creation", "date_maj"),
        }),
    )

    @admin.display(description="Durée confirmée aujourd'hui (min)")
    def duree_confirmee_aujourdhui(self, obj):
        total = RendezVous.objects.filter(
            medecin=obj.medecin,
            statut=RendezVous.Statut.CONFIRME,
            date_rdv__date=timezone.localdate()
        ).aggregate(total=Sum("duree_minutes"))

        return total["total"] or 0

    @admin.action(description="Confirmer les rendez-vous sélectionnés")
    def confirmer_rendezvous(self, request, queryset):
        nombre = queryset.update(statut=RendezVous.Statut.CONFIRME)
        self.message_user(
            request,
            f"{nombre} rendez-vous confirmé(s)."
        )

    @admin.action(description="Annuler les rendez-vous sélectionnés")
    def annuler_rendezvous(self, request, queryset):
        nombre = queryset.update(statut=RendezVous.Statut.ANNULE)
        self.message_user(
            request,
            f"{nombre} rendez-vous annulé(s)."
        )

    actions = ["confirmer_rendezvous", "annuler_rendezvous"]
