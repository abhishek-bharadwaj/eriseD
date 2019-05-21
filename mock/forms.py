from django import forms

from mock.models import Store


class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['data', 'response_delay']
