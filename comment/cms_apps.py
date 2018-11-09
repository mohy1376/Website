from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

@apphook_pool.register
class MyApphook(CMSApp):
    app_name = 'comment'  # must match the application namespace
    name = "EComments"

    def get_urls(self, page=None, language=None, **kwargs):
        return ["comment.urls"] # replace this with the path to your application's URLs module
