from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from . import forms


def render_data(request, return_data):
    return_response_template = loader.get_template('return_response.html')
    context = {

    }
    return HttpResponse(return_response_template.render(context, request))


def post_new(request):
    form = forms.StoreForm()
    return render(request, 'store_mocks.html', {'form': form})
