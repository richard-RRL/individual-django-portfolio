from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Portfolio, Student, Project

admin.site.register(Student)
admin.site.register(Portfolio)
admin.site.register(Project)