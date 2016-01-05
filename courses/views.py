from django.http import HttpResponse
from django.shortcuts import render #for using templates

from .models import Course #imports from models.py
# Create your views here.
def course_list(request):
    courses = Course.objects.all() #selects all courses that exist
    return render(request, 'courses/course_list.html', {'courses': courses}) #takes 3 arguments - request, template to render, optional context dictionary
