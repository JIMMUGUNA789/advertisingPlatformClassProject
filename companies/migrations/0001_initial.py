# Generated by Django 4.1a1 on 2022-12-22 12:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('profilePicture', models.ImageField(blank=True, upload_to='media/')),
                ('bannerPicture', models.ImageField(blank=True, upload_to='media/')),
                ('category', models.CharField(choices=[('Agriculture', 'Agriculture'), ('Mining', 'Mining'), ('Manufacturing', 'Manufacturing'), ('Construction', 'Construction'), ('Wholesale and Retail', 'Wholesale and Retail'), ('Transport', 'Transport'), ('Hospitality', 'Hospitality'), ('Technology', 'Technology'), ('Finance', 'Finance'), ('Real Estate', 'Real Estate'), ('Education', 'Education'), ('Health', 'Health'), ('Entertainment', 'Entertainment'), ('Others', 'Others')], default='Others', max_length=255)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('websiteUrl', models.URLField()),
                ('latitude', models.DecimalField(decimal_places=15, max_digits=15, null=True)),
                ('longitude', models.DecimalField(decimal_places=15, max_digits=15, null=True)),
                ('address', models.CharField(max_length=255)),
                ('operatingHours', models.JSONField()),
                ('companyAdmin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
                ('rating', models.PositiveSmallIntegerField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.companyprofile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.companyprofile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Follows',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.companyprofile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.companyprofile')),
            ],
        ),
    ]
