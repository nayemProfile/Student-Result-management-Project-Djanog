from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


class UserCreateForm(UserCreationForm):
    class Meta:
        model = Custom_User
        fields = UserCreationForm.Meta.fields
        
        
        
class UserLoginForm(AuthenticationForm):
    class Meta:
        model = Custom_User
        fields = ['username', 'password']















class Student_Form(forms.ModelForm):
    
    class Meta:
        model = Student_Model
        fields = ('__all__')
             
    
class Subject_Form(forms.ModelForm):
    
    class Meta:
        model = Subject_Model
        fields = ('__all__')
        
        
class Grade_Form(forms.ModelForm):
    
    class Meta:
        model = Grade_Model
        fields = ('__all__')
        exclude = {'cgpa'}