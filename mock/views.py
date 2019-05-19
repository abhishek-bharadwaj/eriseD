from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from mock import public


def render_data(request, url):
    return_response_template = loader.get_template('return_response.html')
    context = {

    }
    return HttpResponse(return_response_template.render(context, request))
