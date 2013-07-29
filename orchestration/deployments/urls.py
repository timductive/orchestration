from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url

from orchestration.deployments.views import IndexView


urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='deployments'),
)
