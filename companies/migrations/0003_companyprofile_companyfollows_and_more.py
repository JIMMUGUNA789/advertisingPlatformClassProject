# Generated by Django 4.1a1 on 2023-01-12 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_alter_companyimages_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyprofile',
            name='companyFollows',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='companyprofile',
            name='companyLikes',
            field=models.IntegerField(default=0),
        ),
    ]
