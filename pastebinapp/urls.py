from django.conf.urls import url

from . import views

app_name='pastebinapp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # // ex. /5
    url(r'^(?P<snip_id>[0-9]+)/$', views.code, name='code'),
    # // ex. /edit_snip/5
    url(r'^edit_snip/(?P<snip_id>[0-9]+)/$', views.edit_snip, name='edit_snip'),
    # // ex. /enter_snip
    url(r'enter_snip', views.enter_snip, name='enter_snip'),
    # // ex. /compile_snip/1
    url(r'^compile_snip/(?P<snip_id>[0-9]+)/$', views.compile_snip, name='compile_snip'),
]
