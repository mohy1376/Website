from django.conf.urls import url
from . import views
app_name = "contact"
urlpatterns = [
    url(r'^about/', views.about.as_view(), name='about'),

]