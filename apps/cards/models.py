# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Card(models.Model):
    """A class describing information regarding Cards."""
    name = models.CharField(max_length=50)
    # wont let me add min_value...
    cost = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)