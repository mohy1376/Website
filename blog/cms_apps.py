# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from aldryn_apphooks_config.app_base import CMSConfigApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

from .models import NewsBlogConfig


class NewsBlogApp(CMSConfigApp):
    name = _('NewsBlog')
    app_name = 'aldryn_newsblog'
    app_config = NewsBlogConfig

    def get_urls(self, *args, **kwargs):
        return ['aldryn_newsblog.urls']

    # NOTE: Please do not add a «menu» here, menu’s should only be added by at
    # the discretion of the operator.


apphook_pool.register(NewsBlogApp)
