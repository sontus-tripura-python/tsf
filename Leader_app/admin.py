from django.contrib import admin
from Leader_app.models import *
# Register your models here.
@admin.register(CentralYear)
class CentralYearAdmin(admin.ModelAdmin):
    list_display = ['yearname']

@admin.register(CentralMember)
class CentralMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'Posting','session', 'phone']
    list_editable = ['session', 'Posting']
    list_filter = ['session']

@admin.register(BranchYear)
class BranchYearAdmin(admin.ModelAdmin):
    list_display = ['branchyear', 'branches']
    list_filter = ['branches']

@admin.register(BranchMember)
class BranchMemberAdmin(admin.ModelAdmin):
    list_display = [ 'name', 'Posting', 'namebranch', 'memberbranch']
    list_editable = ['Posting', 'namebranch', 'memberbranch' ]
    list_filter = ['namebranch', 'memberbranch']


@admin.register(BranchName)
class BranchNameAdmin(admin.ModelAdmin):
    list_display = ['branchname']