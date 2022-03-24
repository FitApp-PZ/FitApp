from django.shortcuts import render
from django.db.models import Sum, Q
from datetime import date

from activities.models import Activity
from hydration.models import Water

# Create your views here.
def index(request):
    return render(request, 'website/index.html')

def samples(request):
    sum_of_water_today = Water.objects.filter(user=request.user, date=date.today()).aggregate(s=Sum('real_value'))['s']
    sum_of_water_today = 0 if sum_of_water_today is None else sum_of_water_today

    sum_of_activities_today = Activity.objects.filter(user=request.user, date=date.today()).aggregate(s=Sum('duration_time'))['s']
    sum_of_activities_today = 0 if sum_of_activities_today is None else sum_of_activities_today
    
    


    context = {
        'sum_of_water_today': sum_of_water_today/1000,
        'sum_of_activities_today': sum_of_activities_today
    }
    return render(request, 'website/samples.html', context=context)

def BMI_calculator(request):
    return render(request, 'website/BMI_calculator.html')