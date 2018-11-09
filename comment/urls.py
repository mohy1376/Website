from django.conf.urls import url
from . import views
app_name = "comment"
urlpatterns = [
    url(r'^about/', views.about.as_view(), name='about'),
]