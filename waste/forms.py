from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import WasteItem
import base64

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class WasteItemForm(forms.ModelForm):
    image = forms.ImageField(required=False, help_text='Upload an image (optional)')
    
    class Meta:
        model = WasteItem
        fields = ['description', 'location', 'image', 'is_recycle']
        widgets = {
            'is_recycle': forms.CheckboxInput(),
        }
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        image_file = self.cleaned_data.get('image')
        
        # Convert uploaded image to base64
        if image_file:
            image_data = image_file.read()
            base64_image = base64.b64encode(image_data).decode('utf-8')
            instance.image = f'data:image/jpeg;base64,{base64_image}'
        
        if commit:
            instance.save()
        return instance