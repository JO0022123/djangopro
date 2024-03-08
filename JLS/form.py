from django import forms
from . models import Member,User
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):
    class Meta(object):
        model = Member
        fields = ("username","email","password")

class CustomUserForm(UserCreationForm):
    
    class Meta:
        model=User
        fields=['username','email','password1','password2']