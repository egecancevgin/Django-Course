from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse
from datetime import date, datetime
from .models import Course, Category
from django.core.paginator import Paginator
from courses.forms import CourseCreateForm


def index(request):
    courses = Course.objects.filter(isActive=1, isHome=1)
    categories = Category.objects.all()

    return render(request, 'courses/index.html', {
        'categories': categories,
        'courses': courses 
    })

def create_course(request):
    if request.method == "POST":
        form = CourseCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/courses")
    else:
        form = CourseCreateForm()
    
    return render(request, "courses/create-course.html", {"form":form})

def course_list(request):
    courses = Course.objects.all()
    return render(
        request, 'courses/course-list.html',
        {
            'courses': courses
        }
    )

def course_edit(request, id):
    pass

def search(request):
    if 'q' in request.GET and request.GET['q'] != '':
        q = request.GET['q']  
        courses = Course.objects.filter(isActive=True, title__contains=q).order_by('date')
        categories = Category.objects.all()
    else:
        return redirect('/courses')

    return render(request, 'courses/search.html', {
        'categories': categories,
        'courses': courses,
    })
    

def details(request, slug):
    course = get_object_or_404(Course, slug=slug)
    context = {
        'course': course
    }
    return render(request, 'courses/details.html', context)


def getCoursesByCategory(request, slug):
    courses = Course.objects.filter(categories__slug=slug, isActive=True).order_by('date')
    categories = Category.objects.all()

    paginator = Paginator(courses, 1)
    page = request.GET.get('page', 1)
    page_obj = paginator.page(page)

    return render(request, 'courses/list.html', {
        'categories': categories,
        'page_obj': page_obj,
        'chosenCategory': slug
    })

