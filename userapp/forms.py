from django import forms
from .models import*
from django.forms import ModelForm

class PostContentForm(forms.ModelForm):
    author=forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model=PostContent
        fields="__all__"