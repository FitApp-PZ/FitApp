from django.shortcuts import render
from django.db.models import Sum, Q
from datetime import date

from activities.models import Activity
from hydration.models import Water
from sleep.models import Sleep
from body_measurments.models import BodyMeasurements

# Create your views here.
def index(request):
    return render(request, 'website/index.html')

def info(request):
    return render(request, 'website/info.html')

def dashboard(request):
    sum_of_water_today = Water.objects.filter(user=request.user, date=date.today()).aggregate(s=Sum('real_value'))['s']
    sum_of_water_today = 0 if sum_of_water_today is None else sum_of_water_today

    sum_of_activities_today = Activity.objects.filter(user=request.user, date=date.today()).aggregate(s=Sum('duration_time'))['s']
    sum_of_activities_today = 0 if sum_of_activities_today is None else sum_of_activities_today

    sum_of_sleep_today = Sleep.objects.filter(user=request.user, date=date.today()).values('duration_time').aggregate(s=Sum('duration_time'))['s']
    sum_of_sleep_today = 0 if sum_of_sleep_today is None else sum_of_sleep_today
    
    sleep_aim = 8
    width_of_sleep_bar = (sum_of_sleep_today / sleep_aim) * 100
    width_of_sleep_bar = 100 if width_of_sleep_bar > 100 else width_of_sleep_bar


    activities_aim = 60
    width_of_activities_bar = (sum_of_activities_today / activities_aim) * 100
    width_of_activities_bar = 100 if width_of_activities_bar > 100 else width_of_activities_bar


    water_aim = 2000
    width_of_water_bar = (sum_of_water_today / water_aim) * 100
    width_of_water_bar = 100 if width_of_water_bar > 100 else width_of_water_bar

    current_weight = BodyMeasurements.objects.filter(user = request.user).values('weight').order_by('-date').first()['weight']
    


    context = {
        'sum_of_water_today': sum_of_water_today/1000,
        'sum_of_activities_today': sum_of_activities_today,
        'sum_of_sleep_today': sum_of_sleep_today,
        'width_of_sleep_bar': width_of_sleep_bar,
        'width_of_activities_bar': width_of_activities_bar,
        'width_of_water_bar': width_of_water_bar,
        'current_weight': current_weight
    }
    return render(request, 'website/dashboard.html', context=context)

def BMI_calculator(request):
    return render(request, 'website/BMI_calculator.html')