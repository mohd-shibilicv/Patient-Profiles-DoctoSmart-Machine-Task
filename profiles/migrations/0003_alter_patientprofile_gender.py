# Generated by Django 5.0.6 on 2024-06-29 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_patientprofile_phone_numeber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10),
        ),
    ]
