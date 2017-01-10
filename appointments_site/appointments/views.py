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
    template_name = 'appointments.html'

    def get(self, request, *args, **kwargs):
        add_form = AppointmentForm(self.request.GET or None)
        search_form = AppointmentSearchForm(self.request.GET or None)
        print request.GET.get('keyword', None)
        data = self.get_context_data(**kwargs)
        data['add_form'] = add_form
        data['search_form'] = search_form
        data_requests = request.POST.copy()
        keyword = data_requests.get('keyword', None)
        print "AJAX", self.request.is_ajax(), keyword
        if self.request.is_ajax():
            self.template_name = "search_results.html"
            keyword = data_requests.get('keyword', None)
            print "IN", keyword
            if keyword:
                appointments, count = AppointmentsListResource().get_matching_appointments(keyword)
            else:
                appointments, count = ([], -1)
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
        print "SUCESSS"
        return HttpResponseRedirect('%s?success=1'% reverse('home'))
