from django.shortcuts import render

# Create your views here.
def BMI_calculator(request):
    context = {}

    return render(request, 'calculators/BMI_calculator.html')
