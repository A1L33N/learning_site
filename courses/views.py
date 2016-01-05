from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render #for using templates, get_object_or_404 is for handling 404s

from .models import Course #imports from models.py
# Create your views here.
def course_list(request):
    courses = Course.objects.all() #selects all courses that exist
    return render(request, 'courses/course_list.html', {'courses': courses}) #takes 3 arguments - request, template to render, optional context dictionary

def course_detail(request, pk):
    #course = Course.objects.get(pk = pk) pk is primary key/id, don't need now because of 404
    course = get_object_or_404(Course, pk = pk)
    return render(request, 'courses/course_detail.html', {'course': course})
