# Generated by Django 3.2.7 on 2021-09-13 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0014_project_git_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='git_page',
            field=models.CharField(default='https://github.com', max_length=250),
        ),
    ]
