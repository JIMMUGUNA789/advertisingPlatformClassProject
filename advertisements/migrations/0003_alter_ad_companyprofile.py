# Generated by Django 3.2 on 2023-02-27 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0008_alter_companyprofile_operatinghours'),
        ('advertisements', '0002_ad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='companyProfile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='advertisements', to='companies.companyprofile'),
        ),
    ]
