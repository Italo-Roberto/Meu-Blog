from django import forms
from .models import Projeto

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['titulo', 'descricao', 'detalhes', 'tecnologias', 'link', 'foto']