from django.shortcuts import render, redirect

from .models import Project, Cv, My_mail


# Create your views here.
def home_redirect(request):
    return redirect('/home')


def home(request):
    try:
        cvs = Cv.objects.all()
    except Exception as e:
        raise e
    return render(request, 'home.html', {'cvs': cvs})


def projects(request):
    try:
        projects = Project.objects.all()
    except Exception as e:
        raise e
    return render(request, 'project.html', {'projects': projects})


def feedback(request):
    try:
        info_mail = My_mail.objects.all()
    except Exception as e:
        raise e
    return render(request, 'feedback.html', {'info_mail': info_mail})


def project_detail(request, category_slug, project_slug):
    try:
        project = Project.objects.get(category__slug=category_slug, slug=project_slug)
    except Exception as e:
        raise e
    return render(request, 'project_detail.html', {'project': project})
