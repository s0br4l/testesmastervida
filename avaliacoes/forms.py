from django import forms
from django.forms import ModelForm
from .models import Antropometria, Dexa, Testes

class AntropometriaForm(ModelForm):
    class Meta:
        model = Antropometria
        fields = ('peso', 'estatura', 'Ptronco', 'Pcintura', 'Pabdomen', 'Pquadril', 'PantebracoD', 'PbracoD', 'PcoxaD', 'PpernaD')

        widgets = {
            'peso': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Medida em kg'}),
            'estatura': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Medida em cm'}),
            'Ptronco': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Medida em cm'}),
            'Pcintura': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Medida em cm'}),
            'Pabdomen': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Medida em cm'}),
            'Pquadril': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Medida em cm'}),
            'PantebracoD': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Medida em cm'}),
            'PbracoD': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Medida em cm'}),
            'PcoxaD': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Medida em cm'}),
            'PpernaD': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Medida em cm'}),
        }


class TestesForm(ModelForm):
    class Meta:
        model = Testes
        fields = ('Dinamometro_1', 'Dinamometro_2', 'Sentar_levantar', 'Ir_vir_1', 'Ir_vir_2', 'Marcha_1', 'Marcha_2')

        widgets = {
            'Dinamometro_1': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Desempenho em kgf'}),
            'Dinamometro_2': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Desempenho em kgf'}),
            'Sentar_levantar': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Número de repetições'}),
            'Ir_vir_1': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Desempenho em segundos'}),
            'Ir_vir_2': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Desempenho em segundos'}),
            'Marcha_1': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Desempenho em segundos'}),
            'Marcha_2': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Desempenho em segundos'}),
        }

