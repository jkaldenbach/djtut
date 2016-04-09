from django.conf.urls import url
from . import views

app_name = 'programs'
urlpatterns = [
    # /initiatives/
    url(r'^$', views.index, name='index'),
]
