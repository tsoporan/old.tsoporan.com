from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'', include('portfolio.urls')), 
    (r'^admin/', include(admin.site.urls)),

    #For development only:
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}), 
)
