from django.shortcuts import render

# Create your views here.

def home(request):
    return render (request,'home.html')

def courses(request):
    return render(request,'courses.html')

def bootcamp(request):
    return render(request,'bootcamp.html')

def request_callback(request):
    return render(request,'request_callback.html')

def signin(request):
    return render (request,'signin.html')

def form(request):
    return render(request,'form.html')

def freelearning(request):
    return render(request,'freelearning.html')