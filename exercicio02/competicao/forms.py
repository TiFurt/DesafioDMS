from django import forms
from .models import Time, Disputa


class TimeForm(forms.ModelForm):
    class Meta:
        model = Time
        fields = ['nome']


class DisputaForm(forms.ModelForm):
    class Meta:
        model = Disputa
        fields = ['data', 'horario', 'local', 'time01', 'gols01', 'time02', 'gols02']



