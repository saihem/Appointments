from django.conf.urls import include, url
from appointments.views import AppointmentsView


urlpatterns = [
    # Examples:
    url(r'^$', AppointmentsView.as_view(), name='home'),
    # url(r'^appointments_site/', include('appointments_site.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
