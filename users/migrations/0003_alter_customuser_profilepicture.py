# Generated by Django 4.1a1 on 2023-01-12 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profilePicture',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
    ]
