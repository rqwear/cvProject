from django.contrib import admin
from .models import Category, Project, Cv, My_mail

# Register your models here.
admin.site.register(Category)
admin.site.register(Project)
admin.site.register(Cv)
admin.site.register(My_mail)
