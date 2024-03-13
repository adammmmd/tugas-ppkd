   
from django import forms
from .models import BeritaModel
 
 
# creating a form
class BeritaForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = BeritaModel
 
        # specify fields to be used
        fields = [
            "title",
            "author",
            "description",
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'id': 'title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'id': 'author'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'id': 'description'}),
        }
