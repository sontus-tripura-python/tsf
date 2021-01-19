from django.shortcuts import render
from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from Home_app.models import *
from Profile_app.models import *
from News_app.models import *
from About_app.models import *
import json
from django.http import JsonResponse
from django.db.models import Q
def home(request):
    about_inform = TsfAboutSetting.objects.get(id=1)
    sliders = Slider.objects.all()
    student_categories = StudentCategory.objects.all()
    about_categories = Category.objects.all()
    lastes_news = News.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')[:4]
    context = {'student_categories':student_categories, 'about_categories': about_categories,'about_inform':about_inform,
              'sliders': sliders, 'lastes_news': lastes_news }
    return render(request, 'home_app/home.html', context)

def studentscategory(request, pk):
    about_inform = TsfAboutSetting.objects.get(id=1)
    about_categories = Category.objects.all()
    students = StudentCategory.objects.get(pk=pk)
    students_category = Profile.objects.all().filter(current_enroll__exact=students)
    students_category_count = Profile.objects.filter(current_enroll__exact=students).count()
    # print("student", students_category_count)
    context = {'students': students,
    'students_category': students_category, 'students_category_count': students_category_count,
     'about_categories': about_categories,'about_inform':about_inform}
    return render(request, 'home_app/students_categorys.html', context)

# def category_student_details(request, pk):
#     about_categories = Category.objects.all()
#     about_inform = TsfAboutSetting.objects.get(id=1)
#     student = get_object_or_404(Profile, pk=pk)
#     return render(request, 'home_app/students_category_details.html', 
#     context={'student': student, 'about_inform':about_inform, 'about_categories': about_categories,})


def search_students(request):
    if request.method == 'POST':
        search = json.loads(request.body).get('searchTextValue')
        profiles = Profile.objects.filter(
             user__first_name__istartswith=search)| Profile.objects.filter(user__last_name__istartswith=search)
        data = profiles.values()
        return JsonResponse(list(data), safe=False)


def search_list_student(request):
    about_inform = TsfAboutSetting.objects.get(id=1)
    query = request.GET['query']
    allquery = Profile.objects.filter(user__first_name__icontains=query) | Profile.objects.filter(
                                               user__last_name__icontains = query) | Profile.objects.filter(
                                                   college__icontains=query) | Profile.objects.filter(
                                                       deparment__icontains=query
                                                   )| Profile.objects.filter(
                                                       university__icontains=query
                                                   ) | Profile.objects.filter(
                                                       School__icontains=query
                                                   )
    return render(request, 'Profile_app/search.html',
        context={'allquery': allquery, 'query': query,'about_inform':about_inform, })