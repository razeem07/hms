from django import forms
from  hmsapp import models


class ContactForm(forms.ModelForm):

    class Meta:

        model=models.ContactRequest
        fields='__all__'

        widgets = {
            'first_name':forms.TextInput({'class':'border-1 border-gray-400 rounded p-2 hover:none'}),
            'last_name':forms.TextInput({'class':'border-1 border-gray-400 rounded p-2 hover:none'}),
             'email':forms.TextInput({'class':'border-1 border-gray-400 rounded p-2 hover:none'}),
             'phone_number':forms.TextInput({'class':'border-1 border-gray-400 rounded p-2 hover:none'}),
             'message':forms.Textarea({'class':'border-1 border-gray-400 rounded p-2 hover:none','rows':5}),
        }