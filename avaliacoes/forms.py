from django import forms
from django.forms import ModelForm
from .models import Testes_medidas

class CadastroForm(ModelForm):
    class Meta:
        model = Testes_medidas
        fields = ('nome',)
        labels = {
            'nome': 'Nome completo ',
        }

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Como consta no documento'}),
        }


class AntropometriaForm(ModelForm):
    class Meta:
        model = Testes_medidas
        fields = ('peso', 'estatura', 'Ptronco', 'Pcintura', 'Pabdomen', 'Pquadril', 'PantebracoD', 'PbracoD', 'PcoxaD', 'PpernaD')
        labels = {
            'peso': 'Peso (em kg)',
            'estatura': 'Estatura (em cm)',
            'Ptronco': 'Ptronco (em cm)',
            'Pcintura': 'Pcintura (em cm)',
            'Pabdomen': 'Pabdomen (em cm)',
            'Pquadril': 'Pquadril (em cm)',
            'PantebracoD': 'PantebracoD (em cm)',
            'PbracoD': 'PbracoD (em cm)',
            'PcoxaD': 'PcoxaD (em cm)',
            'PpernaD': 'PpernaD (em cm)',
        }

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
        model = Testes_medidas
        fields = ('Dinamometro_1', 'Dinamometro_2', 'Sentar_levantar', 'Ir_vir_1', 'Ir_vir_2', 'Marcha_1', 'Marcha_2')
        labels = {
            'Dinamometro_1': 'Dinamometro - 1 (kgf)',
            'Dinamometro_2': 'Dinamometro - 2 (kgf)',
            'Sentar_levantar': 'Sentar e Levantar (Nrepetições)',
            'Ir_vir_1': 'Ir e vir - 1 (segundos)',
            'Ir_vir_2': 'Ir e vir - 2 (segundos)',
            'Marcha_1': 'Marcha usual - 1 (segundos)',
            'Marcha_2': 'Marcha usual - 2 (segundos)',
        }


        widgets = {
            'Dinamometro_1': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Desempenho em kgf'}),
            'Dinamometro_2': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Desempenho em kgf'}),
            'Sentar_levantar': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Número de repetições'}),
            'Ir_vir_1': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Desempenho em segundos'}),
            'Ir_vir_2': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Desempenho em segundos'}),
            'Marcha_1': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Desempenho em segundos'}),
            'Marcha_2': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Desempenho em segundos'}),
        }


class DexaForm(ModelForm):
    class Meta:
        model = Testes_medidas
        fields = ('BMC_gr', 'FAT_MASS_gr', 'LEAN_MASS_gr', 'DXG_T', 'BMC_Arm_L', 'BMC_Arm_R', 'BMC_Trunk', 'BMC_Leg_L',
                  'BMC_Leg_R', 'BMC_Head', 'FAT_MASS_Arm_L', 'FAT_MASS_Arm_R', 'FAT_MASS_Trunk', 'FAT_MASS_Leg_L',
                  'FAT_MASS_Leg_R', 'FAT_MASS_Head', 'LEAN_MASS_Arm_L', 'LEAN_MASS_Arm_R', 'LEAN_MASS_Trunk',
                  'LEAN_MASS_Leg_L', 'LEAN_MASS_Leg_R', 'LEAN_MASS_Head', 'DXG_FAT_Arm_L', 'DXG_FAT_Arm_R',
                  'DXG_FAT_Trunk', 'DXG_FAT_Leg_L', 'DXG_FAT_Leg_R', 'DXG_FAT_Head', 'Area_L_ARM_cm3', 'Area_R_ARM_cm3',
                  'Area_L_Ribs_cm3', 'Area_R_Ribs_cm3', 'Area_T_Spine_cm3', 'Area_L_Spine_cm3', 'Area_Pelves_cm3',
                  'Area_L_Leg_cm3', 'Area_R_Leg_cm3', 'Area_head_cm3', 'Area_Total_cm3', 'BMD_L_Arm', 'BMD_R_Arm',
                  'BMD_L_Ribs', 'BMD_R_Ribs', 'BMD_T_Spine', 'BMD_L_Spine', 'BMD_Pelves', 'BMD_L_Leg', 'BMD_R_Leg',
                  'BMD_Head', 'BMD_Total', 'T_Score', 'Z_Score')

        widgets = {
            'BMC_gr': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'FAT_MASS_gr': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'LEAN_MASS_gr': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'DXG_T': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'BMC_Arm_L': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'BMC_Arm_R': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'BMC_Trunk': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'BMC_Leg_L': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'BMC_Leg_R': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'BMC_Head': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'FAT_MASS_Arm_L': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'FAT_MASS_Arm_R': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'FAT_MASS_Trunk': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'FAT_MASS_Leg_L': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'FAT_MASS_Leg_R': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'FAT_MASS_Head': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'LEAN_MASS_Arm_L': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'LEAN_MASS_Arm_R': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'LEAN_MASS_Trunk': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'LEAN_MASS_Leg_L': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'LEAN_MASS_Leg_R': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'LEAN_MASS_Head': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'DXG_FAT_Arm_L': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'DXG_FAT_Arm_R': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'DXG_FAT_Trunk': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'DXG_FAT_Leg_L': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'DXG_FAT_Leg_R': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'DXG_FAT_Head': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'Area_L_ARM_cm3': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'Area_R_ARM_cm3': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'Area_L_Ribs_cm3': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'Area_R_Ribs_cm3': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'Area_T_Spine_cm3': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'Area_L_Spine_cm3': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'Area_Pelves_cm3': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'Area_L_Leg_cm3': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'Area_R_Leg_cm3': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'Area_head_cm3': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'Area_Total_cm3': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'BMD_L_Arm': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'BMD_R_Arm': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'BMD_L_Ribs': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'BMD_R_Ribs': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'BMD_T_Spine': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'BMD_L_Spine': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'BMD_Pelves': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'BMD_L_Leg': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'BMD_R_Leg': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'BMD_Head': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'BMD_Total': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'T_Score': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'Z_Score': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}),
        }

