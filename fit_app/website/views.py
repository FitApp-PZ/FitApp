from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'website/index.html')

def samples(request):
    return render(request, 'website/samples.html')

def BMI_calculator(request):
    return render(request, 'website/BMI_calculator.html')