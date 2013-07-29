from django.conf.urls import patterns, include, url

from orchestration.home.views import IndexView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^home/', include('orchestration.home.urls')),
    url(r'^launch/', include('orchestration.launch.urls')),
    url(r'^deployments/', include('orchestration.deployments.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
