from django import forms
from django.contrib.auth.models import User
from .models import profile

class UserRegistrationForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name (Ex: Rupant Akare )'}))
    account_no = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 20231'}))
    aadhar_no = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 1234 5678 1234'}))
    pan_no = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: ABCDE1234A'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email (Ex: test@gmail.com )'}))
    mobile = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 1234567890'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter prefered name (Ex: rupant )'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'}))
    birthday = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 2018-12-31', 'type': 'date'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter address'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter city'}))
    state = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter state'}))
    zip = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 441904'}))
    #admission_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 2018-12-31', 'type': 'date'}))
    
    def clear_form_data(self):
        # Clear the form data
        self.cleaned_data = {}
    
    class Meta:
        model = profile
        fields = ['name', 'account_no', 'aadhar_no','pan_no','email','mobile','username','password','birthday','address','city','state','zip',]