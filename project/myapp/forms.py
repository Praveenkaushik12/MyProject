from django import forms
from django.contrib.auth.models import User
from .models import Doctor, Patient,MedicalData

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ('specialization',)

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('date_of_birth',)

class MedicalReport(forms.ModelForm):
    class Meta:
        model=MedicalData
        fields='__all__'
        exclude=['patient']
        widgets={
            'condition':forms.TextInput(attrs={'class':'form-control'}),
            'treatments':forms.TextInput(attrs={'class':'form-control'}),
            'add_info':forms.TextInput(attrs={'class':'form-control'}),
            'date_of_diag':forms.DateInput(attrs={'class':'form-control','id':'datepicker'}),    
        }
        
