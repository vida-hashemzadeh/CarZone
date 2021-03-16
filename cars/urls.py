
from django.urls import path
from . import views

urlpatterns = [
    path ('cars',views.cars,name='url_cars'),
    path ('<int:id>' , views.car_detail , name = 'url_car_detail'),
    path ('cars/search' , views.search ,name='serach' ),
]
