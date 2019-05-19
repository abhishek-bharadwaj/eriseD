from django.conf.urls import url
from django.utils import timezone

from tastypie.resources import ModelResource
from tastypie.utils.urls import trailing_slash

from mock.models import Store
from mock import public
from mock import views

from . import forms


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
            url(r'^(?P<resource_name>%s)/create%s$' %
                (self.Meta.resource_name, trailing_slash()),
                self.wrap_view('create_mock'), name='create_and_store_mock'),
        ]

    def get_data(self, request, **kwargs):
        self.method_check(request, ['get'])
        searched_url = request.GET['url'].strip()
        return views.render_data(request, public.get_json_data_for_url(searched_url) or {})

    def create_mock(self, request, **kwargs):
        return views.post_new(request)
        # if request.method == "POST":
        #     form = forms.AddressForm(request.POST)
        #     if form.is_valid():
        #         post = form.save(commit=False)
        #         post.author = request.user
        #         post.published_date = timezone.now()
        #         post.save()
        #         return self.create_response(request, {'message': 'Mock created successfully..'})
        # else:
        #     form = forms.AddressForm()
        # return render(request, 'blog/post_edit.html', {'form': form})
