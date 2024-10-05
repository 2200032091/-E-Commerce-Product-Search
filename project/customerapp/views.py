from django.shortcuts import render

# Create your views here.


def customerhomepage(request):
    return render(request,'customer/customerhomepage.html')

def categories(request):
    return render(request,'customer/categories.html')


def homeaccessories(request):
    return render(request, 'customer/homeaccessories.html')


def mobiles(request):
    return render(request, 'customer/mobiles.html')

def shirts(request):
    return render(request, 'customer/shirts.html')