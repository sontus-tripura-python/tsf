from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from About_app.models import *
from Home_app.models import *
# Create your views here.
def about_category_details(request, pk):
     about_inform = TsfAboutSetting.objects.get(id=1)
     categories = Category.objects.get( pk=pk)
     categories_details = About.objects.filter(category=categories)
     context = {'categories_details': categories_details, 'about_inform': about_inform}
     return render(request, 'about_app/about.html', context)