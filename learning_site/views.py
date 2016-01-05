# from django.http import HttpResponse

from django.shortcuts import render #changed to import render from import HttpResponse after adding template folder

def home_page(request):
    return render(request, 'home.html')
