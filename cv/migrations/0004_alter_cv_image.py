# Generated by Django 3.2.7 on 2021-09-09 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0003_cv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='image',
            field=models.ImageField(upload_to='cv_foto'),
        ),
    ]
