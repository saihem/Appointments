# -*- coding: utf-8 -*-
# Django
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.http import JsonResponse

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

class MainView(TemplateView):
    '''
    renders forms and sends data to display search results
    '''
    template_name = 'appointments.html'

    def get(self, request, *args, **kwargs):
        add_form = AppointmentForm(self.request.GET or None)
        search_form = AppointmentSearchForm(self.request.GET or None)
        data = self.get_context_data(**kwargs)
        data['add_form'] = add_form
        data['search_form'] = search_form
        ajax_request = request.GET.copy()
        keyword = ajax_request.get('keyword', None)
        print request.GET.get('keyword', None), "AJAX", self.request.is_ajax(), keyword
        if self.request.is_ajax():
            self.template_name = "search_results.html"
            keyword = ajax_request.get('keyword', None)
            if keyword:
                appointments, count = AppointmentsListResource().get_matching_appointments(keyword)
            else:
                # Returns all appointments because keyword is None
                today = datetime.datetime.today()
                appointments, count = AppointmentsListResource()._get(today)
            print "stuff", appointments, count
            data['appointments'] = appointments
            data['count'] = count
        return self.render_to_response(data)

def validate_keyword(request):
    keyword = request.GET.get('keyword', None)
    appointments, count = AppointmentsListResource().get_matching_appointments(keyword)
    data = {'appointments': appointments, 'count': count}
    return JsonResponse(data)

class AppointmentsView(FormView):
    '''
    Add Appointments
    '''
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
        context.update({'appointments': appointments, "total": total_apps})
        return context

    def form_valid(self, form):
        app_date = form.cleaned_data['date']
        AppointmentsInstanceResource()._post(form.cleaned_data)
        return HttpResponseRedirect('%s?success=1'% reverse('home'))
