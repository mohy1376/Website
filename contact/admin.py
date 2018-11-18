# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import comment , Message
# Register your models here.
@admin.register(comment)
@admin.register(Message)

# admin.site.register(comment)
class AuthorAdmin(admin.ModelAdmin):
    pass