# from django.shortcuts import render
# from .models import Team
# # Create your views here.
# def home (request):
#     team =  Team.objects.all()
#     data = {
#     'teams':team
#     }
#     return render(request, 'pages/home.html',data)

# def about (request):
#       team =  Team.objects.all()
#     data = {
#     'teams':team
#     }
#     return render(request, 'pages/about.html',data)

# def services (request):
#     return render(request,'pages/services.html')

# def contact (request):
#     return render(request, 'pages/contact.html')
    

from django.shortcuts import render
from .models import Team

# Create your views here.
def home(request):
    return render(request, 'pages/home.html', {'teams': Team.objects.all()})

def about(request):
    return render(request, 'pages/about.html', {'teams': Team.objects.all()})

def services(request):
    return render(request, 'pages/services.html', {'teams': Team.objects.all()})

def contact(request):
    return render(request, 'pages/contact.html', {'teams': Team.objects.all()})
