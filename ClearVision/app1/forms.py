from django import forms
from django.forms import ModelForm,TextInput
from django.contrib.auth.forms import UserCreationForm
from app1.models import *

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username','email','phone_no','gender','birthday','password1','password2','joind_date','joind_time')

class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = ['userid','is_active','full_name','useremail','house_no','colony_name','city_name','pincode','state','country','joind_date','joind_time']
        widgets = {
            'full_name' : TextInput(attrs={
                'class': "form-control",
                'style': 'font-size: 17px !important;',
                'placeholder': 'Enter your full name',
                'required': ''
            }),
            'useremail' : TextInput(attrs={
                'class': "form-control",
                'style': 'font-size: 17px !important;',
                'placeholder': 'Enter your email',
                'required': ''
            }),
            'house_no' : TextInput(attrs={
                'class': "form-control",
                'style': 'font-size: 17px !important;',
                'placeholder': 'Enter your house no. / building name',
                'required': ''
            }),
            'colony_name' : TextInput(attrs={
                'class': "form-control",
                'style': 'font-size: 17px !important;',
                'placeholder': 'Enter your colony/area/road name',
                'required': ''
            }),
            'city_name' : TextInput(attrs={
                'class': "form-control",
                'style': 'font-size: 17px !important;',
                'placeholder': 'Enter your village/city name',
                'required': ''
            }),
            'pincode' : TextInput(attrs={
                'class': "form-control",
                'style': 'font-size: 17px !important;',
                'placeholder': 'Enter your pincode',
                'required': ''
            }),
        }

class WishlistTableForm(ModelForm):
    class Meta:
        model = WishlistTable
        fields = ['id','user_id','goggles_id']