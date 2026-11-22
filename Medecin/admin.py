
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm

from .models import Medecin, Specialite


class MedecinCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Medecin
        fields = ('username', 'matricule_ordre', 'telephone')


@admin.register(Medecin)
class MedecinAdmin(UserAdmin):
    add_form = MedecinCreationForm

    add_fieldsets = (
        (None, {
            'fields': (
                'username',
                'matricule_ordre',
                'telephone',
                'password1',
                'password2',
            ),
        }),
    )

    fieldsets = UserAdmin.fieldsets + (
        ('Médecin', {
            'fields': (
                'matricule_ordre',
                'telephone',
                'specialites',
            ),
        }),
    )

    list_display = (
        'username',
        'matricule_ordre',
        'first_name',
        'last_name',
        'telephone',
    )

    search_fields = [
        'matricule_ordre',
        'last_name',
        'first_name',
    ]

    filter_horizontal = ['specialites']

    def get_readonly_fields(self, request, obj=None):
        readonly = list(super().get_readonly_fields(request, obj))
        if obj is not None:
            readonly.append('matricule_ordre')
        return readonly


@admin.register(Specialite)
class SpecialiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom_specialite')
    search_fields = ['nom_specialite']
