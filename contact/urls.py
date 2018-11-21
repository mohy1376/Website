from django.conf.urls import url
from . import views
app_name = "contact"
urlpatterns = [
    url(r'^about/', views.about.as_view(), name='about'),
    url(r'^accounts/', views.UserFormView.as_view(), name='accounts'),
    url(r'logout/', views.logOut , name='logout')

]