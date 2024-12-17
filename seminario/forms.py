from django import forms
from .models import Inscrito

class InscritoForm(forms.ModelForm):
    class Meta:
        model = Inscrito
        fields = '__all__'

    def clean_nro_personas(self):
        nro = self.cleaned_data['nro_personas']
        if nro < 1 or nro > 30:
            raise forms.ValidationError("El número de personas debe estar entre 1 y 30.")
        return nro

    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']
        if not telefono.isdigit():
            raise forms.ValidationError("El teléfono debe contener solo números.")
        return telefono
