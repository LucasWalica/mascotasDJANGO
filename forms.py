from django import forms

from .models import Mascota

class PetCreateForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ('nombre','tipo_de_sprite')
        