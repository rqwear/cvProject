# Generated by Django 3.2.7 on 2021-09-13 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0015_alter_project_git_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='git_page',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='project',
            name='git_page',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
