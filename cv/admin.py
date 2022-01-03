from django.contrib import admin
from .models import Category, Project, Cv, My_mail, Certificate

# Register your models here.
admin.site.register(Category)
admin.site.register(Project)
admin.site.register(Cv)
admin.site.register(My_mail)
admin.site.register(Certificate)
