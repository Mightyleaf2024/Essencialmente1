from django import forms
from .models import Avaliar_IMC

class Avaliar_IMCModelForm(forms.ModelForm):
    class Meta:
        model = Avaliar_IMC
        fields = ['cpf','nome','sexo','data_nasc','escola','peso','altura','imagem']