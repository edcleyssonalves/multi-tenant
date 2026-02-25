from django import forms
from . import models


class ProductForm(forms.ModelForm):

    class Meta:
        model = models.Product
        fields = ['title', 'value']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'value': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Produto',
            'value': 'Valor',
        }
