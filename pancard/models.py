# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.core.exceptions import ValidationError
from django.db import models


class KycDocuments(models.Model):
    class Meta:
        verbose_name_plural = 'KycDocuments'

    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    pan_number = models.CharField(max_length=10, null=False, blank=False)
    dob = models.DateField(null=False, blank=False)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(self, KycDocuments).save(force_insert=force_insert, force_update=force_update,
                                       using=using, update_fields=update_fields)
        if self.dob < datetime.date(1900, 01, 01):
            raise ValidationError("DOB must be greater than 1900")