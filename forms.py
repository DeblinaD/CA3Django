from django.forms import ModelForm
from django import forms
from datetime import date
from .import models
from django.contrib.auth.forms import AuthenticationForm


class DatePickerInput(forms.DateInput):
        input_type = 'date'




class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = models.UserProfile
        fields = ['username', 'email', 'password']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class UserForm(ModelForm):
    

    class Meta:
        model = models.User
        fields = '__all__'

class RecordForm(ModelForm):
    

    class Meta:
        model =models.Record
        fields = '__all__'
        widgets = {
            'Date' : DatePickerInput(),
            'user_id': forms.TextInput(attrs={'placeholder': 'Enter User ID'}),
}