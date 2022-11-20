from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from App_login.models import UserProfile
from django.forms import ModelForm

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True,label='Email Address')
    class Meta:
        model = User
        fields = ('username','email','password1','password2')


class UserProfileChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','password')

class ProfilePic(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_pic',)