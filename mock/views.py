from django.shortcuts import render

from . import forms


def render_create_mock_view(request):
    if request.method == 'POST':
        form = forms.StoreForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'mock_creation_success.html')

    form = forms.StoreForm
    return render(request, 'store_mocks.html', {'form': form})
