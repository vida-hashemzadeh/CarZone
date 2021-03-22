from django.shortcuts import render
from .models import Team
from cars.models import Car

# Create your views here
def home(request):
    teams = Team.objects.all()
    featured_car=Car.objects.order_by ('created_date').filter(is_featured=True)
    latest_car = Car.objects.order_by('created_date')
    all_cars = Car.objects.order_by ('id')

    # fields = Car.objects.values('model','year')
    model_cars= Car.objects.values_list('model',flat=True).distinct() ,
    city_cars= Car.objects.values_list('city',flat=True).distinct() ,
    year_cars= Car.objects.values_list('year',flat=True).distinct() ,
    body_style_cars= Car.objects.values_list ('body_style',flat=True).distinct() ,

    data={
        'teams':teams,
        'featured_car':featured_car ,
        'latest_car': latest_car ,
        'all_cars':all_cars,
        'model_cars':model_cars,
        'city_cars':city_cars ,
        'year_cars':year_cars ,
        'body_style_cars':body_style_cars ,


    }
    return render(request,'pages/home.html',data)
# -------------------------------------------------------------
def about(request):
    teams=Team.objects.all()
    data = {
        'teams':teams
    }
    return render(request,'pages/about.html',data)
# -------------------------------------------------------------


def services(request):
    return render(request , 'pages/services.html')
# -------------------------------------------------------------

def contact(request):
    return render(request,'pages/contact.html')
