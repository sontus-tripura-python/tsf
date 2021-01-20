from django.contrib import admin

# Register your models here.
from News_app.models import *

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_date', 'publish_date']


admin.site.register(Comment)
