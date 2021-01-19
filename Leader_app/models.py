from django.db import models

# Create your models here.
class CentralYear(models.Model):
    yearname = models.CharField(max_length=30)

    def __str__(self):
        return self.yearname

    class Meta:
        verbose_name_plural = "central year"

class CentralMember(models.Model):

    STATUS = (

    ('University', 'University'),
    ('College', 'College'),
    ('School', 'School'),
    ('Job', 'Job'),
    ('Other', 'Other'),
    )
    session = models.ForeignKey(CentralYear, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='central', blank=True)
    name = models.CharField(max_length=50, blank=True)
    Posting = models.CharField(max_length=50, blank=True)
    blood_group = models.CharField(max_length=20, blank=True)
    phone = models.CharField(max_length=11, blank=True)
    village = models.CharField(max_length=200, blank=True)
    thana = models.CharField(max_length=200, blank=True)
    district = models.CharField(max_length=200, blank=True)
    gender = models.CharField(max_length=20, default="Male", choices=(("Male", "Male"), ("Female", "Female")))
    current_enroll = models.CharField(max_length=200, null=True, choices=STATUS)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    linkdin = models.URLField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Central Member'

class BranchName(models.Model):
    branchname = models.CharField(max_length=200)

    def __str__(self):
        return self.branchname
    class Meta:
        verbose_name_plural = "Branch Name"

class BranchYear(models.Model):
    branchyear = models.CharField(max_length=200)
    branches = models.ForeignKey(BranchName, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-id',)


    def __str__(self):
        return f"{self.branchyear } of {self.branches}"

    class Meta:
        verbose_name_plural = "Branch year"

class BranchMember(models.Model):

    STATUS = (

    ('University', 'University'),
    ('College', 'College'),
    ('School', 'School'),
    ('Job', 'Job'),
    ('Other', 'Other'),
    )
    memberbranch = models.ForeignKey(BranchYear, null=True, blank=True, on_delete=models.CASCADE)
    namebranch = models.ForeignKey(BranchName, null=True, blank=True, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='branchmember', blank=True)
    University = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=50, blank=True)
    Posting = models.CharField(max_length=50, blank=True)
    blood_group = models.CharField(max_length=20, blank=True)
    phone = models.CharField(max_length=11, blank=True)
    gender = models.CharField(max_length=20, default="Male", choices=(("Male", "Male"), ("Female", "Female")))
    current_enroll = models.CharField(max_length=200, null=True, choices=STATUS)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    linkdin = models.URLField(blank=True)

    class Meta:
        ordering = ('id',)
        verbose_name_plural = "Branch member"

    def __str__(self):
        return f"{self.name } of {self.memberbranch}"


class Coordinator(models.Model):
    photo = models.ImageField(upload_to='branchmember', blank=True)
    name = models.CharField(max_length=50, blank=True)
    position = models.CharField(max_length=200, blank=True)
    blood_group = models.CharField(max_length=20, blank=True)
    phone = models.CharField(max_length=11, blank=True)
    about_description = models.TextField()
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    linkdin = models.URLField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Co-ordinator"
