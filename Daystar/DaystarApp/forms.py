from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class BabyForm(forms.ModelForm):
    class Meta:
        model = Baby
        fields = ['B_name', 'c_stay', 'Gender', 'age', 'fathers_name', 'mothers_name','location','mothers_phone', 'fathers_phone','brought_by','timeIn', 'timeOut','baby_number', 'assign']
        labels = {
            'B_name': 'Baby Name',
            'c_stay': 'Category',
            'Gender': 'Gender',
            'age': 'Age',
            'fathers_name': 'Fathers Name',
            'mothers_name': 'Mothers Name',
            'location': 'Location',
            'brought_by': 'Brought By',
            'timeIn': 'Time In',
            'timeOut': 'Time Out',
            'baby_number': 'Baby Number',
            'assign': 'Assign',
            'fathers_phone': 'Fathers Phone',
            'mother_phone':'Mothers Phone',
        }
        widgets = {
            'B_name': forms.TextInput(attrs={'class': 'form-control'}),
            'c_stay': forms.Select(attrs={'class': 'form-control'}),
            'Gender': forms.Select(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'fathers_name': forms.TextInput(attrs={'class': 'form-control'}),
            'mothers_name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'brought_by': forms.TextInput(attrs={'class': 'form-control'}),
            'timeIn': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'timeOut': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'baby_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'assign': forms.TextInput(attrs={'class': 'form-control'}),
            'fathers_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'mother_phone': forms.TextInput(attrs={'class': 'form-control'}),
        }


class SittersForm(forms.ModelForm):
    class Meta:
        model = Sitter
        fields = ['S_name', 'Gender', 'NIN', 'recommenders_name', 'next_of_kin','location','contact', 'religion','education_level','sitter_number']
        labels = {
            'S_name': 'Sitter Name',
            'Gender': 'Gender',
            'recommenders_name': 'Recommenders Name',
            'location': 'Location',
            'next_of_kin': 'Next of Kin',
            'religion': 'religion',
            'education_level': 'Education Level',
            'sitter_number': 'Sitter Number',
            'contact': 'Contact',
            'NIN': 'NIN',
           
        }
        widgets = {
            'S_name': forms.TextInput(attrs={'class': 'form-control'}),
            'Gender': forms.Select(attrs={'class': 'form-control'}),
            'recommenders_name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'next_of_kin': forms.TextInput(attrs={'class': 'form-control'}),
            'religion': forms.Select(attrs={'class': 'form-control'}),
            'education_level': forms.Select(attrs={'class': 'form-control'}),
            'sitter_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            'NIN': forms.TextInput(attrs={'class': 'form-control'}),
           
           
            
        }

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['S_name', 'payment_type', 'amount', 'date_of_payment']



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']




















# class SitterForm(forms.Form):
#         GENDER_CHOICES = (
#         ('Male', 'Male'),
#         ('Female', 'Female'),
#     )
#         RELIGION_CHOICES = (
#         ('Christian', 'Christian'),
#         ('Muslim', 'Muslim'),
#         ('Other', 'Other'),
#     )
#         EDUCATION_LEVEL_CHOICES = (
#         ('Primary', 'Primary'),
#         ('Secondary', 'Secondary'),
#         ('University', 'University'),
#     )
#         S_name = models.CharField(max_length=200, widget= forms.TextInput(attrs={'class': 'form-control'}),required=False)
#         Gender = models.CharField(max_length=10,choices=GENDER_CHOICES, widget= forms.TextInput(attrs={'class': 'form-control'}),required=False)
#         dob = models.DateTimeField(auto_now_add=True, widget= forms.TextInput(attrs={'class': 'form-control'}),required=False)
#         location = models.CharField(max_length=200, default="Kabalaga", widget= forms.TextInput(attrs={'class': 'form-control'}),required=False)
#         next_of_kin = models.CharField(max_length=200, widget= forms.TextInput(attrs={'class': 'form-control'}),required=False)
#         recommenders_name = models.CharField(max_length=200, widget= forms.TextInput(attrs={'class': 'form-control'}),required=False)
#         religion = models.CharField(max_length=100, choices=RELIGION_CHOICES, blank=True, widget= forms.TextInput(attrs={'class': 'form-control'}),required=False)
#         NIN = models.CharField(max_length=30, unique=True, widget= forms.TextInput(attrs={'class': 'form-control'}),required=False)
#         education_level = models.CharField(max_length=200, choices=EDUCATION_LEVEL_CHOICES, widget= forms.TextInput(attrs={'class': 'form-control'}),required=False)
#         sitter_number = models.CharField(max_length=200, unique=True, widget= forms.TextInput(attrs={'class': 'form-control'}),required=False)
#         contact = models.IntegerField(null= True, widget= forms.TextInput(attrs={'class': 'form-control'}),required=False)
#         def clean(self):
#         cleaned_data = super().clean()
#         task_name = cleaned_data.get('task_name')
#         details = cleaned_data.get('details')
#         no_of_people = cleaned_data.get('no_of_people')
#         #date_created = cleaned_data.get('date_created')
#         day_of_week = cleaned_data.get('day_of_week')

#         if not task_name:
#             self.add_error('task_name', 'Please provide a task name')
#         elif len(task_name) <3:
#             self.add_error('task_name', 'Name must be at least 3 characters')
#         return cleaned_data