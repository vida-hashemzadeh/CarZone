from django.urls import path
from . import views

urlpatterns = [
    path ('login' , views.login , name = 'url_login'),
    path ('register',views.register, name ='url_register'),
    path ('logout',views.logout, name ='url_logout'),
    path ('dashboard',views.dashboard, name ='url_dashboard'),

]
