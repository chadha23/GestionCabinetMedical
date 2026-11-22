from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm

from .models import Patient
from RendezVous.models import RendezVous


class PatientCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Patient
        fields = (
            'username',
            'cin',
            'telephone',
            'date_naissance',
        )


class RendezVousInline(admin.TabularInline):
    model = RendezVous
    fk_name = 'patient'
    extra = 0
    show_change_link = True


@admin.register(Patient)
class PatientAdmin(UserAdmin):

    add_form = PatientCreationForm

    add_fieldsets = (
        (None, {
            'fields': (
                'username',
                'cin',
                'telephone',
                'date_naissance',
                'password1',
                'password2',
            ),
        }),
    )

    fieldsets = UserAdmin.fieldsets + (
        ('Patient', {
            'fields': (
                'cin',
                'telephone',
                'date_naissance',
            )
        }),
    )

    list_display = (
        'username',
        'cin',
        'first_name',
        'last_name',
        'telephone',
    )

    search_fields = [
        'last_name',
        'first_name',
        'cin',
    ]

    def get_readonly_fields(self, request, obj=None):
        readonly = list(super().get_readonly_fields(request, obj))

        if obj is not None:
            readonly.append('cin')

        return readonly

    inlines = [RendezVousInline]
