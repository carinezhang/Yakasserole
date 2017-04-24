"""
Definition of urls for Yakaserver.
"""

from datetime import datetime
from django.conf.urls import include, url
from django.contrib import admin
import django.contrib.auth.views
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.urls import staticfiles.urlpatterns
 urlpatterns += staticfile_urlpatterns()

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about', app.views.about, name='about'),
    url(r'^login/$',
         django.contrib.auth.views.login,
         {
             'template_name': 'app/login.html',
             'authentication_form': app.forms.BootstrapAuthenticationForm,
             'extra_context':
             {
                 'title': 'Log in',
                 'year': datetime.now().year,
             }
         },
         name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            
            'next_page': '/',
        },
        name='logout'),

    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/profile/$', RedirectView.as_view(pattern_name='home', permanent=False)),


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
     url(r'^admin/', admin.site.urls),
]
