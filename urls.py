from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'fruit.app.views.home_view'),
    url(r'^account/$', 'fruit.app.views.account_view'),
    url(r'^login/$', 'fruit.app.views.login_view'),
    url(r'^registration/$', 'fruit.app.views.registration_view'),
    url(r'^logout/$', 'fruit.app.views.logout_view'),
    url(r'^price/$', 'fruit.app.views.price_view'),
    url(r'^info/$', 'fruit.app.views.info_view'),
    url(r'^cart/$', 'fruit.app.views.cart_view'),
    url(r'^news/$', 'fruit.app.views.news_view'),
    url(r'^buy/(\d+)/$', 'fruit.app.views.buy_view'),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()