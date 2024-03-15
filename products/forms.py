from django import forms
from django.contrib.auth.forms import UserCreationForm

from products.models import ContactRequest, Client


class ContactRequestForm(forms.ModelForm):
    class Meta:
        model = ContactRequest
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            # set rows=5 for Textarea
            if field.widget.__class__ == forms.widgets.Textarea:
                field.widget.attrs['rows'] = '5'

            # set form-control class for all widgets
            if 'class' in field.widget.attrs:
                field.widget.attrs['class'] = ' ' 'form-control'
            else:
                field.widget.attrs.update({'class': 'form-control'})


class ClientForm(UserCreationForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            # set rows=3 for Textarea
            if field.widget.__class__ == forms.widgets.Textarea:
                field.widget.attrs['rows'] = '3'

            # set form-control class for all widgets
            if 'class' in field.widget.attrs:
                field.widget.attrs['class'] = ' ' 'form-control'
            else:
                field.widget.attrs.update({'class': 'form-control'})
