# Generated by Django 3.2.7 on 2021-09-13 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0009_alter_my_mail_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='phase_project',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
