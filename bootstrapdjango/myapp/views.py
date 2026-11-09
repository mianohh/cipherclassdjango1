from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def service(request):
    return render(request, 'service.html')

def fruit(request):
    return render(request, 'fruit.html')

def contact(request):
    return render(request, 'contact.html')

