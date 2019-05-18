from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from django.db import models

from common.models import BaseModel


class Store(BaseModel):
    username = models.ForeignKey(User, related_name='mocks', on_delete=models.CASCADE, null=True)
    url = models.CharField(max_length=100, primary_key=True)
    data = JSONField()
    response_delay = models.IntegerField()
