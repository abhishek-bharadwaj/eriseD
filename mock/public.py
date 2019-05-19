from django.core.exceptions import ObjectDoesNotExist

from mock.models import Store


def get_json_data_for_url(url):
    try:
        return Store.objects.get(url=url).to_json()
    except ObjectDoesNotExist:
        return None
