from django import forms
from datetime import date
from .models import Recipe


class RecipeModelForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
