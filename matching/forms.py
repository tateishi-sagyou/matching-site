from django import forms

from .models import User

class PostForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('user_id', 'user_password','user_name')

class LoginForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('user_id', 'user_password')