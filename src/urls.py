from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

from blog.views import MySearchView

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^search/', MySearchView()),

)
