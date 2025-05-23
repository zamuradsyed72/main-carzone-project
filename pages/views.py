from django.shortcuts import render
from .models import Team
from cars.models import Car

# Create your views here.
def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date')
    

    context = {
        'teams': teams,
        'featured_cars': featured_cars,
        'all_cars': all_cars,
    }
    return render(request, 'pages/home.html', context)

def about(request):
    return render(request, 'pages/about.html', {'teams': Team.objects.all()})

def services(request):
    return render(request, 'pages/services.html', {'teams': Team.objects.all()})

def contact(request):
    return render(request, 'pages/contact.html', {'teams': Team.objects.all()})
