from django import forms
from .models import Professor
from .models import Disciplina
from .models import SalaDeAula
from .models import Turma

class FormProfessor(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['nome', 'cpf']
class FormTurma(forms.ModelForm):
    class Meta:
        model = Turma
        fields = ['nome']

class FormDisciplina(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = ['nome', 'carga_horaria_total']

class FormSala(forms.ModelForm):
    class Meta:
        model = SalaDeAula
        fields = ['nome']
