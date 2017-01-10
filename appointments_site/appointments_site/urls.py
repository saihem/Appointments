from django.conf.urls import include, url
from appointments.views import MainView
from appointments.views import AppointmentsView
from appointments.views import validate_keyword
#from appointments.views import AppointmentsSearchView


urlpatterns = [
    url(r'^$', MainView.as_view(), name='home'),
    url(r'^add/', AppointmentsView.as_view(), name='add'),
    url(r'^search/', validate_keyword, name='search'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
