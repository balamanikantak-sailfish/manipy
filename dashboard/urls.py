from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import goedits.views

# Examples:
# url(r'^$', 'dashboard.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
	 url(r'^$', goedits.views.index, name='index'),
	 url(r'^compare/$', goedits.views.compare, name='compare'),
	 url(r'^pricing/$',goedits.views.pricing, name='pricing'),
	 url(r'^contact$',goedits.views.contact, name='contact'),
     url(r'^admin', include(admin.site.urls))
]
