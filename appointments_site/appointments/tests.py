from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse

from appointments.models import Appointment

import datetime

# Create your tests here.

class AppointmentsTest(TestCase):
	fixtures = ['initial_data.json']
	client = Client()
	response = client.get(reverse('home'))
	response.status_code
    response = client.get(reverse('search'))
    response.status_code
    appointment = Appointment(text='Django', date=datetime.datetime.today())
	appointment.save()