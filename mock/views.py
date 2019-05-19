from django.http import HttpResponse
from django.shortcuts import render

from mock import public


def get_data(request, url):
    store_obj = public.get_json_data_for_url(url)
    if store_obj:
        return HttpResponse(store_obj)
    else:
        return HttpResponse("The json equivalent to {} doesn't exist.".format(url))
