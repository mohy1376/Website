# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import comment
# Register your models here.
@admin.register(comment)
# admin.site.register(comment)
class AuthorAdmin(admin.ModelAdmin):
    pass