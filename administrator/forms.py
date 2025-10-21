from django import forms
from .models import Department,HealthPackage,Insurance



class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['department_name', 'slug', 'description', 'image']
        
        widgets = {
            'department_name': forms.TextInput(attrs={
                'class': 'border border-gray-400 rounded p-2 w-full',
                'placeholder': 'Enter department name'
            }),
            'slug': forms.TextInput(attrs={
                'class': 'border border-gray-400 rounded p-2 w-full',
                'placeholder': 'Enter slug (unique)'
            }),
            'description': forms.Textarea(attrs={
                'class': 'border border-gray-400 rounded p-2 w-full',
                'rows': 4,
                'placeholder': 'Write a short description...'
            }),
            'image': forms.FileInput(attrs={
                'class': 'border border-gray-400 rounded p-2 w-full'
            }),
        }



class HealthPackageForm(forms.ModelForm):
    class Meta:
        model =  HealthPackage
        fields = ['name', 'slug', 'description', 'image']
        
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'border border-gray-400 rounded p-2 w-full',
                'placeholder': 'Enter package name'
            }),
            'slug': forms.TextInput(attrs={
                'class': 'border border-gray-400 rounded p-2 w-full',
                'placeholder': 'Enter slug (unique)'
            }),
            'description': forms.Textarea(attrs={
                'class': 'border border-gray-400 rounded p-2 w-full',
                'rows': 4,
                'placeholder': 'Write a short description...'
            }),
            'image': forms.FileInput(attrs={
                'class': 'border border-gray-400 rounded p-2 w-full'
            }),
        }

class InsuranceForm(forms.ModelForm):
    class Meta:
        model =  Insurance
        fields = ['name', 'slug', 'description', 'image']
        
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'border border-gray-400 rounded p-2 w-full',
                'placeholder': 'Enter Insurance name'
            }),
            'slug': forms.TextInput(attrs={
                'class': 'border border-gray-400 rounded p-2 w-full',
                'placeholder': 'Enter slug (unique)'
            }),
            'description': forms.Textarea(attrs={
                'class': 'border border-gray-400 rounded p-2 w-full',
                'rows': 4,
                'placeholder': 'Write a short description...'
            }),
            'image': forms.FileInput(attrs={
                'class': 'border border-gray-400 rounded p-2 w-full'
            }),
        }