from django import forms
from .models import Todo

class Form_View(forms.ModelForm):
    texts = forms.CharField(max_length= 40)

    class Meta:
        model = Todo
        fields = [
            'texts',
            
           
        ]
    