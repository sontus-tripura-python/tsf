from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import *
from Home_app.models import *
from Leader_app.models import *
# Create your views here.
def branch_name(request):
    about_inform = TsfAboutSetting.objects.get(id=1)
    branchs = BranchName.objects.order_by('-id')
    context = { 'branchs': branchs, 'about_inform':about_inform}
    return render(request, 'Leader_app/branch_name_list.html', context )

def branch_form(request):
    about_inform = TsfAboutSetting.objects.get(id=1)
    if request.method == 'POST':
        form = BranchForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Branch name has been added successfully')
            return redirect('branch_name')
    else:
        form = BranchForm()
        context = {'form': form,  'about_inform':about_inform}
    return render(request, 'Leader_app/branch_form.html', context)
          
def branch_name_update(request, pk):
    about_inform = TsfAboutSetting.objects.get(id=1)
    branch = get_object_or_404(BranchName, pk=pk)
    if request.method == 'POST':
        form = BranchForm(request.POST, instance=branch)
        if form.is_valid():
            form.save()
            messages.info(request, 'Branch name has been added successfully')
            return redirect('branch_name')
    else:
        form = BranchForm(instance=branch)
        context = {'form': form, 'about_inform':about_inform } 
    return render(request, 'Leader_app/branch_form.html', context)

def branch_delete(request, pk):
    branch = get_object_or_404(BranchName, pk=pk)
    branch.delete()
    return redirect('branch_name')

def branch_year(request, pk):
    about_inform = TsfAboutSetting.objects.get(id=1)
    branch = BranchName.objects.get(pk=pk)
    branchyears = BranchYear.objects.all().filter(branches=branch)
    context = {'branch': branch , 'branchyears': branchyears, 'about_inform':about_inform}
    return render(request, 'Leader_app/branch_year.html', context )

def branch_year_form(request, pk):
    about_inform = TsfAboutSetting.objects.get(id=1)
    branchname = BranchName.objects.get(id=pk)
    if request.method == 'POST':
        form = BranchYearForm(request.POST)
        if form.is_valid():
            print(form)
            form_year = form.save(commit=False)
            form_year.branches = branchname
            form_year.save()
            messages.info(request, 'branch year has been added successfully')
            return HttpResponseRedirect(reverse('branch_year', args=(branchname.pk,)))
    else:
        form = BranchYearForm()
        context = {'form': form, 'branchname': branchname, 'about_inform':about_inform}
    return render(request, 'Leader_app/branch_year_form.html', context)


def branch_year_update(request, pk):
    about_inform = TsfAboutSetting.objects.get(id=1)
    year = get_object_or_404(BranchYear, pk=pk)
    if request.method == 'POST':
        form = BranchYearForm(request.POST, instance=year)
        if form.is_valid():
            form.save()
            messages.info(request, 'branch year has been updated successfully')
            return HttpResponseRedirect(reverse('branch_year', args=(year.branches.pk,)))
            # return redirect('branch_name')
    else:
        form = BranchYearForm(instance=year)
        context = {'form': form, 'year': year, 'about_inform':about_inform}
    return render(request, 'Leader_app/branch_year_form.html', context)

def branch_year_delete(request, pk):
    year = get_object_or_404(BranchYear, pk=pk)
    year.delete()
    # return HttpResponseRedirect(reverse('branch_year', args=(year.pk)))
    return redirect('branch_name')

def branch_member(request, pk):
    about_inform = TsfAboutSetting.objects.get(id=1)
    branch_member = BranchYear.objects.get(pk=pk)
    members = BranchMember.objects.filter(memberbranch=branch_member)
    context = { 'members': members, 'branch_member': branch_member, 'about_inform':about_inform}
    print(members)
    return render(request, 'Leader_app/branch_members_list.html', context)


def add_member_form(request, pk):
    about_inform = TsfAboutSetting.objects.get(id=1)
    branch_year = BranchYear.objects.get(id=pk)
    form = MemberAddForm(initial={'branch_year': branch_year})
    if request.method == 'POST':
        form = MemberAddForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.memberbranch = branch_year
            obj.save()
            messages.info(request, 'Branch leader has been added successfully')
            return HttpResponseRedirect(reverse('branch_member', args=(branch_year.pk,)))

    context = { 'form': form, 'about_inform':about_inform}
    return render(request, 'Leader_app/add_member_form.html', context)

def member_details_update(request, pk):
    about_inform = TsfAboutSetting.objects.get(id=1)
    member = get_object_or_404(BranchMember, pk=pk)
    form = MemberAddForm(instance=member)
    if request.method == 'POST':
        form = MemberAddForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            messages.info(request, 'Branch leader has been updated successfully')
            return HttpResponseRedirect(reverse('branch_member', args=(member.memberbranch.pk,)))
    else:
        form = MemberAddForm(instance=member)
    context = { 'form': form, 'about_inform':about_inform}
    return render(request, 'Leader_app/add_member_form.html', context)

def branch_member_delete(request, pk):
    about_inform = TsfAboutSetting.objects.get(id=1)
    branchmember = get_object_or_404(BranchMember, pk=pk)
    branchmember.delete()
    # return redirect('branch_name')
    return HttpResponseRedirect(reverse('branch_member', args=(branchmember.branch_member.pk,)))

def branch_leader_details(request, pk):
    about_inform = TsfAboutSetting.objects.get(id=1)
    Branchdetail = get_object_or_404(BranchMember, pk=pk)
    context = {'Branchdetail': Branchdetail, 'about_inform':about_inform}
    return render(request, 'Leader_app/branch_member_details.html', context)


def central_years(request):
    about_inform = TsfAboutSetting.objects.get(id=1)
    years = CentralYear.objects.order_by('-id')
    context = { 'years': years, 'about_inform':about_inform}
    return render(request, 'Leader_app/central_leader/session_central.html', context )

def central_year_form(request):
    about_inform = TsfAboutSetting.objects.get(id=1)
    if request.method == 'POST':
        form = CentralForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Central year has been added successfully')
            return redirect('central_years')
    else:
        form = CentralForm()
    return render(request, 'Leader_app/central_leader/centralyear_form.html', context={'form': form, 'about_inform':about_inform})


def central_year_update(request, pk):
    about_inform = TsfAboutSetting.objects.get(id=1)
    central_year = get_object_or_404(CentralYear, pk=pk)
    if request.method == 'POST':
        form = CentralForm(request.POST, instance=central_year)
        if form.is_valid():
            form.save()
            messages.info(request, 'Central year has been updated successfully')
            return redirect('central_years')
    else:
        form = CentralForm(instance=central_year)
    return render(request, 'Leader_app/central_leader/centralyear_form.html',
     context={'form': form, 'about_inform':about_inform })

def central_year_delete(request, pk):
    central_year = get_object_or_404(CentralYear, pk=pk)
    central_year.delete()
    return redirect('central_years')

def central_leader(request, pk):
    about_inform = TsfAboutSetting.objects.get(id=1)
    centralyear = CentralYear.objects.get(pk=pk)
    centralLeader = CentralMember.objects.all().filter(session__exact=centralyear)
    context = {'centralyear':centralyear, 'centralLeader': centralLeader, 'about_inform':about_inform }
    return render(request, 'Leader_app/central_leader/central_leader.html', context)

def central_member_form(request, pk):
    about_inform = TsfAboutSetting.objects.get(id=1)
    central_member = CentralYear.objects.get(pk=pk)
    if request.method == 'POST':
        form = CentralMemberForm(request.POST, request.FILES)
        if form.is_valid():
            form_year = form.save(commit=False)
            form_year.session = central_member
            form_year.save()
            messages.info(request, 'Central leader has been added successfully')
            return HttpResponseRedirect(reverse('central_leader', args=(central_member.pk,)))
    else:
        form = CentralMemberForm()
        context = {'form': form, 'central_member': central_member, 'about_inform':about_inform }
    return render(request, 'Leader_app/central_leader/central_member_form.html', context)



def central_leader_details(request, pk):
    about_inform = TsfAboutSetting.objects.get(id=1)
    centraldetail = get_object_or_404(CentralMember, pk=pk)
    context = {'centraldetail': centraldetail, 'about_inform':about_inform}
    return render(request, 'Leader_app/central_leader/central_leader_details.html', context)

def central_leader_update(request, pk):
    about_inform = TsfAboutSetting.objects.get(id=1)
    central_leader = get_object_or_404(CentralMember, pk=pk)
    form = CentralMemberForm(instance=central_leader)
    if request.method == 'POST':
        form = CentralMemberForm(request.POST, request.FILES, instance=central_leader)
        if form.is_valid():
            form.save()
            messages.info(request, 'Branch leader has been updated successfully')
            # return redirect('central_years')
            return HttpResponseRedirect(reverse('central_leader', args=(central_leader.session.pk,)))
    else:
        form = CentralMemberForm(instance=central_leader)
    context = {'form': form, 'central_leader': central_leader, 'about_inform':about_inform}
    return render(request, 'Leader_app/central_leader/central_member_form.html', context)

def central_leader_delete(request, pk):
    central_leader = get_object_or_404(CentralMember, pk=pk)
    central_leader.delete()
    return redirect('central_years')

def co_ordinator(request):
    about_inform = TsfAboutSetting.objects.get(id=1)
    coordinators = Coordinator.objects.all()
    context = {'coordinators': coordinators, 'about_inform':about_inform}
    return render(request, 'Leader_app/co-ordinator/co_ordinator.html', context )

def co_ordinator_details(request, pk):
    about_inform = TsfAboutSetting.objects.get(id=1)
    Coordinatordetail = get_object_or_404(Coordinator, pk=pk)
    context = {'Coordinatordetail': Coordinatordetail, 'about_inform':about_inform}
    return render(request, 'Leader_app/co-ordinator/co_ordinator_details.html', context)

def coordinator_create(request):
    about_inform = TsfAboutSetting.objects.get(id=1)
    if request.method == 'POST':
        form = CoordinatorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, 'co-ordinator has been added successfully')
            return redirect('co_ordinator')
    else:
        form = CoordinatorForm()
        context = {'form': form, 'about_inform':about_inform }
    return render(request, 'Leader_app/co-ordinator/coodinator_create_form.html', context)

def coordinator_update(request, pk):
    about_inform = TsfAboutSetting.objects.get(id=1)
    co_ordinator = get_object_or_404(Coordinator, pk=pk)
    if request.method == 'POST':
        form = CoordinatorForm(request.POST, request.FILES, instance=co_ordinator)
        if form.is_valid():
            form.save()
            messages.info(request, 'co-ordinator has been updated successfully')
            return redirect('co_ordinator')
    else:
        form = CoordinatorForm(instance=co_ordinator)
        context = {'form': form, 'about_inform':about_inform }
    return render(request, 'Leader_app/co-ordinator/coodinator_create_form.html', context)


def co_ordinator_delete(request, pk):
    co_ordinator = get_object_or_404(Coordinator, pk=pk)
    co_ordinator.delete()
    return redirect('co_ordinator')
