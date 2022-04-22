from django.contrib import admin

from .models import *

# Register your models here.
# admin.site.register(Student)
 
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'rank')

