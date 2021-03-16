from django.shortcuts import render , get_object_or_404
from .models import Car
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def cars(request):
    all_car = Car.objects.order_by('id')
    paginator = Paginator(all_car,2)
    page = request.GET.get('page')
    paged_cars = paginator.get_page (page)
    data = {
        'all_car': paged_cars ,
    }
    return render (request,'cars/cars.html',data)

def car_detail (request,id):
    one_car = get_object_or_404 (Car , pk=id)

    data= {
        'one_car': one_car ,
    }
    return render (request,'cars/car_detail.html',data)

def search (request):
    return render (request , 'cars/search.html' )

# Create your views here.
