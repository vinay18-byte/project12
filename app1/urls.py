from django.urls import path
from .views import *

app_name='app1'


urlpatterns =[
    path('',home,name='home'),
    path('courses/',courses,name='courses'),
    path('bootcamp/',bootcamp,name='bootcamp'),
    path('request_callback/', request_callback , name='request_callback'),
    path('signin/',signin, name='signin'),
    path('form/',form, name='form'),
    path('freelearning',freelearning, name='freelearning'),
]