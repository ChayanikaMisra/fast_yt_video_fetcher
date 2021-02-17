"""AutoTimestamped Abstract model

This model can be inherited to give install_ts and update_ts
fields to your django model by default.
"""
from django.db import models


class AutoTimestampedModel(models.Model):
    """AutoTimestampedModel

    This model can be inherited to give install_ts and update_ts
    fields to your django model by default.

    Extends:
        models.Model

    """

    install_ts = models.DateTimeField(auto_now_add=True)
    update_ts = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
