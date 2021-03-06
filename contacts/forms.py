from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name',
            'company_name',
            'address_1',
            'address_2',
            'favorite_color',
            'city',
            'state',
            'zip_code',
            'phone_number',
            'email',
            'birthday',
            'species'
        ]
