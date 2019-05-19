from django.conf.urls import url

from tastypie.resources import ModelResource
from tastypie.utils.urls import trailing_slash

from mock.models import Store
from mock import public
from mock import views


class MockResource(ModelResource):
    class Meta:
        resource_name = 'store'
        object_class = Store
        queryset = Store.objects.all()

    def prepend_urls(self):
        return [
            url(r'^(?P<resource_name>%s)/get_data%s$' %
                (self.Meta.resource_name, trailing_slash()),
                self.wrap_view('get_data'), name='get_json_data_for_url'),
        ]

    def get_data(self, request, **kwargs):
        self.method_check(request, ['get'])
        searched_url = request.GET['url'].strip()
        return views.render_data(request, public.get_json_data_for_url(searched_url) or {})
