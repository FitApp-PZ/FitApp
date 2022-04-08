from calendar import weekday
from datetime import date, datetime, timedelta
from re import template
from urllib import request
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Sum, Q, Count
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from body_measurments.forms import BodyMeasurementsForm
from body_measurments.models import BodyCircuits, BodyMeasurements, Goals

# Create your views here.
class BodyMeasurementsListView(ListView):
    model = BodyMeasurements
    paginate_by = 100
    template_name = 'body_measurements/body_measurements/body_measurements_list.html'
    extra_context = {'today': date.today().strftime('%d/%m/%Y')}

    def get_queryset(self):
        user = self.request.user
        return BodyMeasurements.objects.filter(user=user).order_by('-date')

class BodyMeasurementsDetailView(DetailView):
    model = BodyMeasurements
    template_name = 'body_measurements/body_measurements/body_measurements_detail.html'
    extra_context = {}

    def get_queryset(self):
        user = self.request.user
        return BodyMeasurements.objects.filter(user=user)

class BodyMeasurementsCreateView(CreateView):
    model = BodyMeasurements
    form_class = BodyMeasurementsForm
    template_name = 'body_measurements/body_measurements/body_measurements_form.html'
    extra_context = {}

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        messages.success(self.request, 'Pomiary ciała zostały dodane!')
        return reverse_lazy('body_measurements:body_measurements_list')

class BodyMeasurementsUpdateView(UpdateView):
    model = BodyMeasurements
    form_class = BodyMeasurementsForm
    template_name = 'body_measurements/body_measurements/body_measurements_form.html'
    extra_context = {}

    def get_queryset(self):
        user = self.request.user
        return BodyMeasurements.objects.filter(user=user)

    def get_success_url(self):
        messages.success(self.request, 'Pomiary ciała zostały zaaktualizowane!')
        return reverse('body_measurements:body_measurements_detail', kwargs={'pk': self.object.pk})

class BodyMeasurementsDeleteView(DeleteView):
    model = BodyMeasurements
    template_name = 'body_measurements/body_measurements/body_measurements_confirm_delete.html'
    extra_context = {}

    def get_queryset(self):
        user = self.request.user
        return BodyMeasurements.objects.filter(user=user)

    def get_success_url(self):
        messages.success(self.request, 'Pomiary ciała zostały usunięte!')
        return reverse_lazy('body_measurements:body_measurements_list')

def BodyMeasurementsViewChart(request):
    return render(request, 'body_measurements/body_measurements/body_measurements_chart.html')

def BodyMeasurementsGetChart(request):
    summary_type = request.GET.get('summary_type', 'mon1')

    all_body_measurements = BodyMeasurements.objects.filter(user=request.user).order_by('date')

    date_list = [body_measurements_date['date'] for body_measurements_date in BodyMeasurements.objects.order_by('date').values('date').distinct()]

    if summary_type == 'mon1':
        N = 30
    elif summary_type == 'mon3':
        N = 3 * 30
    elif summary_type == 'mon6':
        N = 6 * 30
    elif summary_type == 'year1':
        N = 12 * 30


    today = datetime.now()    
    #print(today.date())
    n_days_ago = today - timedelta(days=N)

    date_last_time = []

    for i in range(N, -1 ,-1):
        n_days_ago = today - timedelta(days=i)
        date_last_time.append(n_days_ago.date())

    sum_value_at_date = []
    

    for sleep_date in date_last_time:
        activities_tot = BodyMeasurements.objects.filter(user=request.user).aggregate(s=Sum('weight', filter=Q(date=sleep_date)))['s']
        # if activities_tot is None:
        #     sum_value_at_date.append(0)
        # else:
        sum_value_at_date.append(activities_tot)

    #print(sum_value_at_date)

    first_date_of_days = sum_value_at_date[0]
    last_date_of_days = sum_value_at_date[-1]

    return JsonResponse({
        # 'all_sleep': all_body_measurements,
        'label': date_last_time,
        'data': sum_value_at_date,
        # 'first_date_of_14_days': first_date_of_days,
        # 'last_date_of_14_days': last_date_of_days
    })

    #return render(request, 'body_measurements/body_measurements/body_measurements_chart.html', context=context)

