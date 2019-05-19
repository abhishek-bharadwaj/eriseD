from django import forms

from mock.models import Store

STATES = (
    ('', 'Choose...'),
    ('MG', 'Minas Gerais'),
    ('SP', 'Sao Paulo'),
    ('RJ', 'Rio de Janeiro')
)


class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['url', 'data', 'response_delay']
