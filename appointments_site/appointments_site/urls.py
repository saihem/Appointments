from django.conf.urls import include, url
from appointments.views import AppointmentsView
from appointments.views import AppointmentsSearchView


urlpatterns = [
    # Examples:
    url(r'^$', AppointmentsView.as_view(), name='home'),
    url(r'^search/', AppointmentsSearchView.as_view(), name='home'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
