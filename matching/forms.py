from django import forms

from .models import User, UserDetail, UserImage
from django.contrib.auth.forms import AuthenticationForm

class PostForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('user_id', 'user_password')

# class LoginForm(AuthenticationForm):
#     """ログオンフォーム"""
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field in self.fields.values():
#             field.widget.attrs['class'] = 'myfieldclass'
#             field.widget.attrs['placeholder'] = 'user_id'
#             self.fields['user_id'].widget.attrs['class'] = 'myfieldclass'
#             self.fields['user_password'].widget.attrs['class'] = 'myfieldclass'
#             self.fields['user_id'].widget.attrs['class']

class LoginForm(forms.ModelForm):
    
    user_id = forms.CharField(
    widget=forms.TextInput(attrs={'class' : 'myfieldclass',
    'placeholder':'user id'}))
    
    user_password = forms.CharField(
        widget=forms.TextInput(attrs={'class' : 'myfieldclass',
        'placeholder':'password'}))

    class Meta:
        model = User
        fields = ('user_id', 'user_password')


class UpLoadProfileImgForm(forms.Form):
    model = UserImage
    detail_model = UserDetail

    user_images = forms.ImageField(required=True)
    user_name = forms.CharField(required=True)
    user_profile = forms.CharField(required=True)