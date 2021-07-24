from django import forms

from .models import User, UserDetail, UserImage

class PostForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('user_id', 'user_password','user_name')

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