from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from django.db import models

from . import private
from common.models import BaseModel


class Store(BaseModel):
    user = models.ForeignKey(User, related_name='mocks', on_delete=models.CASCADE, null=True)
    url = models.CharField(max_length=100, primary_key=True)
    data = JSONField()
    response_delay = models.IntegerField()

    def save(self, *args, **kwargs):
        self.url = private.generate_url_endpoint()
        super(Store, self).save(*args, **kwargs)

    def to_json(self):
        return {
            'url': self.url,
            'data': self.data,
            'response_delay': self.response_delay
        }

    def __str__(self):
        return str(self.to_json())
