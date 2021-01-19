# Generated by Django 3.1.5 on 2021-01-18 15:45

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
            name='StudentCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_enroll_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, default='default.jpg', upload_to='profile_pic')),
                ('university', models.CharField(blank=True, max_length=100)),
                ('School', models.CharField(blank=True, max_length=100)),
                ('college', models.CharField(blank=True, max_length=100)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=20)),
                ('status', models.CharField(choices=[('Single', 'Single'), ('Married', 'Married'), ('In a Relationship', 'In a Relationship')], default='Single', max_length=30)),
                ('fathername', models.CharField(blank=True, max_length=50)),
                ('mothername', models.CharField(blank=True, max_length=50)),
                ('deparment', models.CharField(blank=True, max_length=50)),
                ('religion', models.CharField(blank=True, max_length=20)),
                ('Class', models.CharField(blank=True, max_length=10)),
                ('Village', models.CharField(blank=True, max_length=150)),
                ('thana', models.CharField(blank=True, max_length=50)),
                ('phone', models.CharField(blank=True, max_length=12)),
                ('district', models.CharField(blank=True, max_length=100)),
                ('current_city', models.CharField(blank=True, max_length=100)),
                ('local_city', models.CharField(blank=True, max_length=100)),
                ('birthday', models.DateField(blank=True, default='1990-02-02', null=True)),
                ('facebook', models.URLField(blank=True)),
                ('twitter', models.URLField(blank=True)),
                ('instagram', models.URLField(blank=True)),
                ('linkdin', models.URLField(blank=True)),
                ('current_enroll', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='current_enroll', to='Profile_app.studentcategory')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]