from django.conf.urls import patterns, include, url

import django_health_check.health_check
django_health_check.health_check.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'django_health_check.health_check.views.home', name='health_check_home'),
)
