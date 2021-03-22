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
    all_car = Car.objects.order_by('id')


# ----------------  search ------------------
    if 'search_keyword' in request.GET :
        keyword = request.GET['search_keyword']
        if keyword:
            all_car= all_car.filter(description__icontains=keyword)
            all_car= all_car.filter(car_title__icontains=keyword)

    if 'model_keyword' in request.GET:
        keyword= request.GET['model_keyword']
        if keyword :
            all_car = all_car.filter(model__iexact = keyword)

    if 'city_keyword' in request.GET:
        keyword= request.GET['city_keyword']
        if keyword :
            all_car = all_car.filter(city__iexact = keyword)

    if 'year_keyword' in request.GET:
        keyword= request.GET['year_keyword']
        if keyword :
            all_car = all_car.filter(year__iexact = keyword)

    if 'body_style_keyword' in request.GET:
        keyword= request.GET['body_style_keyword']
        if keyword :
            all_car = all_car.filter(body_style__icontains = keyword)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']

        if max_price :
            all_car = all_car.filter(price__gte = min_price , price__lte = max_price)

    data = {
        'all_car': all_car
    }
    return render (request , 'cars/search.html' ,data)

# Create your views here.
