from django.db import models
from django.urls import reverse


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='project', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    phase_project = models.CharField(max_length=250)
    git_page = models.CharField(max_length=250, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'project'
        verbose_name_plural = 'projects'

    def __str__(self):
        return self.name


class Cv(models.Model):
    title_name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    cv_text = models.TextField(blank=True)
    image = models.ImageField(upload_to='cv_foto')
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    on_main_page = models.BooleanField(default=False)
    git_page = models.CharField(max_length=250, blank=True)

    class Meta:
        ordering = ('title_name',)
        verbose_name = 'Cv'
        verbose_name_plural = 'Cvs'

    def __str__(self):
        return self.title_name


class My_mail(models.Model):
    mail = models.EmailField(blank=True)
    slug = models.SlugField(max_length=100, unique=True)
    tel = models.TextField(max_length=200, blank=True)
    web = models.TextField(max_length=200, blank=True)
    info = models.TextField(blank=True)

    def __str__(self):
        return self.mail

    class Meta:
        ordering = ('mail',)
        verbose_name = 'My_mail'
        verbose_name_plural = 'My_mails'
