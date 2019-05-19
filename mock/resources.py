from tastypie.resources import ModelResource

from mock.models import Store


class MockResource(ModelResource):
    class Meta:
        queryset = Store.objects.all()
        resource_name = 'store'
