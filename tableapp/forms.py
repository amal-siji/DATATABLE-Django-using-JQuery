from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from . models import *


class Editform(forms.ModelForm):

    class Meta:
        model = Person
        fields = ['name', 'place']


class All(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'place']
