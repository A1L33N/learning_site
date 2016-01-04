from django.http import HttpResponse
from django.shortcuts import render #for using templates

from .models import Course #imports from models.py
# Create your views here.
def course_list(request):
    courses = Course.objects.all() #selects all courses that exist
    output = ', '.join([str(course) for course in courses]) #formats output of courses - in this case, a for loop inside a list?
    return HttpResponse(output) #returns http response
