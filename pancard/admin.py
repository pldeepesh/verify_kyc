# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from pancard.models import KycDocuments


class KycDocumentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name',
                    'pan_number', 'dob')
    list_display_links = ('id',)
    list_filter = ('pan_number', 'first_name', 'last_name')

admin.site.register(KycDocuments, KycDocumentsAdmin)
