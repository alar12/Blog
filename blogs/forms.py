# blog/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import BlogPost  # Import your BlogPost model
from django.core.exceptions import ValidationError
class CustomUserCreationForm(UserCreationForm):

   
    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")

        if len(password1) < 8:
            raise ValidationError("Password must be at least 8 characters long.")

        return password1 
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content']  