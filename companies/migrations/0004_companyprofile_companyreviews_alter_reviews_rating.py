# Generated by Django 4.1a1 on 2023-01-13 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_companyprofile_companyfollows_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyprofile',
            name='companyReviews',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='rating',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1),
        ),
    ]
