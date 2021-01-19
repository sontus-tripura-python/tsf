from django import forms
from Leader_app.models import *

# form all
class CentralForm(forms.ModelForm):
    class Meta:
        model = CentralYear
        fields = '__all__'

class CentralMemberForm(forms.ModelForm):
    class Meta:
        model = CentralMember
        fields = '__all__'
        exclude = ['session', 'slug']

class CoordinatorForm(forms.ModelForm):
    class Meta:
        model = Coordinator
        fields = '__all__'

class BranchForm(forms.ModelForm):
    class Meta:
        model = BranchName
        fields = '__all__'

class BranchYearForm(forms.ModelForm):
    class Meta:
        model = BranchYear
        fields = ('id', 'branchyear')

class MemberAddForm(forms.ModelForm):
    class Meta:
        model = BranchMember
        fields = ('photo', 'name', 'Posting', 'gender', 'University', 'blood_group','phone', 'current_enroll',
                   'facebook', 'instagram', 'twitter', 'linkdin',)
