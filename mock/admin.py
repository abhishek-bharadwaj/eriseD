from django.contrib import admin

from mock.models import Store


class StoreAdmin(admin.ModelAdmin):
    exclude = ('url',)


admin.site.register(Store, StoreAdmin)
