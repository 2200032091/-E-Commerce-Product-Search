from django.shortcuts import render


def homepage(request):
    return render(request,'project/homepage.html')


def adminhomepage(request):
    return render(request,'admin/adminhomepage.html')


def about(request):
    return render(request,'project/about.html')


def shopnow(request):
    return render(request,'project/shopnow.html')


def contact(request):
    return render(request,'project/contact.html')


def login(request):
    return render(request,'project/login.html')
