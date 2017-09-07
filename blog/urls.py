from django.conf.urls import url

from .views import (post_detail, 
					post_list, 
					post_create, 
					post_update,
					post_delete)

urlpatterns = [
  url(r'^(?P<id>\d+)/$', post_detail, name='detail'),
  url(r'^list/$', post_list, name='list'),
  url(r'^create/$', post_create, name='create'),
  url(r'^(?P<id>\d+)/update/$', post_update, name='update'),
  url(r'^(?P<id>\d+)/delete/$', post_delete, name='delete')
]
