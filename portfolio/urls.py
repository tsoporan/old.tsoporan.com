from django.conf.urls.defaults import *

urlpatterns = patterns('', 
    url(r'^$', 'portfolio.views.index', name="index"),
    url(r'^about/$', 'portfolio.views.about', name="about"),
    url(r'^work/$', 'portfolio.views.work', name="work"),
    url(r'^contact/$', 'portfolio.views.contact', name="contact"),
)
