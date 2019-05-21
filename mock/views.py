from django.shortcuts import render

from mock import forms
from mock import private


def render_create_mock_view(request):
    if request.method == 'POST':
        form = forms.StoreForm(request.POST)
        if form.is_valid():
            store = form.save(commit=False)
            store.url = private.generate_url_endpoint()
            store.save()
            return render(request, 'mock_creation_success.html')

    form = forms.StoreForm
    return render(request, 'store_mocks.html', {'form': form})
