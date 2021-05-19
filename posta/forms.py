from django import forms
from .models import Bloga

class CreatePostaForm(forms.ModelForm):
    class Meta:
        model = Bloga
        fields = ['name', 'age', 'body', 'image']
