# Generated by Django 4.1a1 on 2023-01-14 09:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0005_reviews_reviewphoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='reviews',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
