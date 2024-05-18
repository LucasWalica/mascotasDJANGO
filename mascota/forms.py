from django import forms

from .models import Mascota, Items

class PetCreateForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ('nombre','tipo_de_sprite')

class EntretenimientoForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ()
        
class SaciedadForm(forms.ModelForm):
    class Meta:
        model = Mascota 
        fields = ()

class HigieneForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ()
        
class comprarJabones(forms.ModelForm):
    class Meta:
        model = Items
        fields = ()

class comprarJuguetes(forms.ModelForm):
    class Meta:
        model = Items 
        fields = ()

class comprarManzanas(forms.ModelForm):
    class Meta:
        model = Items
        fields = ()