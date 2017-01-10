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

class MainView(TemplateView):
    template_name = 'appointments.html'

    def get(self, request, *args, **kwargs):
        add_form = AppointmentForm(self.request.GET or None)
	search_form = AppointmentSearchForm(self.request.GET or None)
        context = self.get_context_data(**kwargs)
        context['add_form'] = add_form
        context['search_form'] = search_form
        return self.render_to_response(context)

class AppointmentsView(FormView):
	template_name = "appointments.html"
 	form_class = AppointmentForm
 	success_url = '/'

	def get(self, *args, **kwargs):
		form = self.form_class(self.request.POST)
	        return super(AppointmentsView, self).get(self, *args, **kwargs)

	def get_context_data(self, **kwargs):
	    context = super(AppointmentsView, self).get_context_data(**kwargs)
	    today = datetime.datetime.today()
	    appointments, total_apps = AppointmentsListResource()._get(today)
	    print appointments
            context.update({'appointments': appointments, "total": total_apps})
            return context

        def form_valid(self, form):
            app_date = form.cleaned_data['date']
            AppointmentsInstanceResource()._post(form.cleaned_data)
            return HttpResponseRedirect('%s?success=1'% reverse('home'))


class AppointmentsSearchView(FormView):
	template_name = "appointments.html"
	form_class = AppointmentSearchForm
	success_url = '/'

	# def get_form_kwargs(self):
 #            """
 #            Returns the keyword arguments for instantiating the form.
 #            """
 #            kwargs = {'initial': self.get_initial()}
 #            print self.request.GET, self.request.POST
 #            print kwargs, "kwargs"
 #            if self.request.method in ('GET', 'PUT'):
 #                kwargs.update({
 #                    'data': self.request.GET,
 #                    'files': self.request.FILES,
 #                })
 #            return kwargs

	def get(self, *args, **kwargs):
            form = self.form_class(self.request.POST)
            print "FORM", form, self.form_valid(), self.form.cleaned_data
            if form.is_valid():
                return self.form_valid(form)
            else:
                return self.form_invalid(form)
            return super(AppointmentsSearchView, self).get(self, *args, **kwargs)

        def get_context_data(self, **kwargs):
            context = super(AppointmentsSearchView, self).get_context_data(**kwargs)
            if self.appointments:
            	context.update({'appointments': self.appointments, 'count': self.count})
            	print "WE HAVE CONTEXT", context
            return context

        def form_valid(self, form):
            self.query_params = form.cleaned_data
            print "self", self.query_params
            if self.query_params.get('keyword') != u'':
                self.appointments, self.count = AppointmentsListResource().get_matching_appointments(self.query_params)
            else:
                self.appointments, self.count = ([], -1)
            print "LETSSS SEEEEE", self.appointments, self.count
            return self.render_to_response(self.get_context_data(form=form))


