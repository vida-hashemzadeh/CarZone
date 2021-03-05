
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about , name='url-about'),
    path('services',views.services , name='url-services'),
    path('contact',views.contact , name='url-contact'),
]
