from django import forms
from .models import Denuncia

class DenunciaForm(forms.ModelForm):
    class Meta:
        model = Denuncia
        fields = ['nome', 'email', 'descricao']
        widgets = {
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descreva o incidente...'}),
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu nome (opcional)'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Seu email (opcional)'}),
        }
