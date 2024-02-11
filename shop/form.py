from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms
class CustomUserForm(UserCreationForm):
    class Meta:
      
        model=User
        fields=['username','email','password1','password2']

    def __init__(self,*args,**kwargs):
        super(CustomUserForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs.update({'class':'form-control','placeholder':'Enter User Name'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter Email'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter Password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Re-enter Password'})
       