


from django import forms
from .models import CustomUser  # Import your custom user model

class SignUpForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password'] 

        widgets = {'password': forms.PasswordInput()}