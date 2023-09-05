from django import forms
from django.core.exceptions import ValidationError
from .models import *

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'photo', 'category']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username','password')

    def clean_user_name(self):
        user_name =self.cleaned_data['username']
        if user_name == None:
            raise ValidationError('user name nan pa dwe vid')
        if len(user_name)<8:
            raise ValidationError('user name lan two kout')
        return user_name
    
    def clean_password(self):
        password=self.cleaned_data['password']
        if len(password)<8:
            raise ValidationError('password la two kout')
        return password
    

class profilform(forms.ModelForm):
    class Meta:
        model = Profile
        fields ='__all__'
        exclude=['user']