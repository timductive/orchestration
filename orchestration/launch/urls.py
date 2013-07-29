from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url

from orchestration.launch.views import IndexView


urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='launch'),
)
