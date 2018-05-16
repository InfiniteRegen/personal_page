from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'main.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    path('foundation/', include('foundation.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
