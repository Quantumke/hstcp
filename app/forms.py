from django import forms
from .models import contactus

class ContactDetails(forms.ModelForm):

    class Meta:
        model=contactus
        fields=('name', 'email', 'phone', 'message',)
