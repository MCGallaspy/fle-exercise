from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(__package__ + '.views',
    url(r'^$', 'landing_page', {}, 'landing_page'),
    url(r'^movies/(?P<movie_id>\d+)/', 'movie_detail'),
    url(r'^admin/', include(admin.site.urls)),
)
