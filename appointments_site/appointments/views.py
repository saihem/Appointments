# -*- coding: utf-8 -*-
# Django
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.views.generic import View

# Appointments
from appointments.forms import AppointmentForm
from appointments.forms import AppointmentSearchForm
from appointments.api import AppointmentsInstanceResource
from appointments.api import AppointmentsListResource

# Python
import datetime
import json

# Requests
import requests


from appointments.models import Appointment
print "ALL APPS", Appointment.objects.all()
for app in Appointment.objects.all():
	print app.created_on
	print app.date
	print app.description
print "END OF APP STUFF"

class AppointmentsView(FormView):
	template_name = "appointments.html"
 	form_class = AppointmentForm

	def get(self, *args, **kwargs):
	    return super(AppointmentsView, self).get(self, *args, **kwargs)

	def get_context_data(self, **kwargs):
	    context = super(AppointmentsView, self).get_context_data(**kwargs)
	    today = datetime.datetime.today()
	    appointments = AppointmentsListResource()._get(today)
	    print appointments
            context.update({'appointments': appointments})
            return context

        def form_valid(self, form):
            app_date = form.cleaned_data['date']
            AppointmentsInstanceResource()._post(form.cleaned_data)
            return HttpResponseRedirect('%s?success=1'% reverse('home'))

# class AddAppointmentView(FormView):
# 	template_name = "add_appointments.html"
# 	form_class = AppointmentForm

class AppointmentsSearchView(FormView):
	template_name = "search.html"
	form_class = AppointmentSearchForm


