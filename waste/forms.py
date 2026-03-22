from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import WasteItem

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class WasteItemForm(forms.ModelForm):
    class Meta:
        model = WasteItem
        fields = ['description', 'location', 'image', 'is_recycle']
        widgets = {
            'is_recycle': forms.CheckboxInput(),
        }