from django.conf.urls.defaults import *

urlpatterns = patterns('', 
    url(r'^$', 'portfolio.views.index', name='index'),
)
