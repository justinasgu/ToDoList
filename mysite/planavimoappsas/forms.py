from .models import Uzduotis
from django import forms


class DateInput(forms.DateInput):
    input_type = 'sukurta'


class UserUzduotisCreateForm(forms.ModelForm):
    class Meta:
        model = Uzduotis
        fields = ['uzduotis', 'vartotojas', 'sukurta']
        widgets = {'vartotojas': forms.HiddenInput(), 'sukurta': DateInput()}
