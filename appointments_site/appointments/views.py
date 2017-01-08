# -*- coding: utf-8 -*-

# Django
from django.conf import settings
from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

# Appointments
from appointments.forms import AppointmentForm
from appointments.forms import AppointmentSearchForm

# Python
import datetime
import json

# Requests
import requests


class AppointmentsView(FormView):
	template_name = "appointments.html"
	form_class = AppointmentForm
	def get(self, request):
		appointment = 

class AppointmentsSearchView(FormView):
	template_name = "search.html"
	form_class = AppointmentSearchForm

	
