# Generated by Django 3.1.5 on 2021-01-18 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BranchName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branchname', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Branch Name',
            },
        ),
        migrations.CreateModel(
            name='CentralYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yearname', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'central year',
            },
        ),
        migrations.CreateModel(
            name='Coordinator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='branchmember')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('position', models.CharField(blank=True, max_length=200)),
                ('blood_group', models.CharField(blank=True, max_length=20)),
                ('phone', models.CharField(blank=True, max_length=11)),
                ('about_description', models.TextField()),
                ('facebook', models.URLField(blank=True)),
                ('twitter', models.URLField(blank=True)),
                ('instagram', models.URLField(blank=True)),
                ('linkdin', models.URLField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Co-ordinator',
            },
        ),
        migrations.CreateModel(
            name='CentralMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='central')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('Posting', models.CharField(blank=True, max_length=50)),
                ('blood_group', models.CharField(blank=True, max_length=20)),
                ('phone', models.CharField(blank=True, max_length=11)),
                ('village', models.CharField(blank=True, max_length=200)),
                ('thana', models.CharField(blank=True, max_length=200)),
                ('district', models.CharField(blank=True, max_length=200)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=20)),
                ('current_enroll', models.CharField(choices=[('University', 'University'), ('College', 'College'), ('School', 'School'), ('Job', 'Job'), ('Other', 'Other')], max_length=200, null=True)),
                ('facebook', models.URLField(blank=True)),
                ('twitter', models.URLField(blank=True)),
                ('instagram', models.URLField(blank=True)),
                ('linkdin', models.URLField(blank=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Leader_app.centralyear')),
            ],
            options={
                'verbose_name_plural': 'Central Member',
            },
        ),
        migrations.CreateModel(
            name='BranchYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branchyear', models.CharField(max_length=200)),
                ('branches', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Leader_app.branchname')),
            ],
            options={
                'verbose_name_plural': 'Branch year',
            },
        ),
        migrations.CreateModel(
            name='BranchMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='branchmember')),
                ('University', models.CharField(blank=True, max_length=100)),
                ('name', models.CharField(blank=True, max_length=50)),
                ('Posting', models.CharField(blank=True, max_length=50)),
                ('blood_group', models.CharField(blank=True, max_length=20)),
                ('phone', models.CharField(blank=True, max_length=11)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=20)),
                ('current_enroll', models.CharField(choices=[('University', 'University'), ('College', 'College'), ('School', 'School'), ('Job', 'Job'), ('Other', 'Other')], max_length=200, null=True)),
                ('facebook', models.URLField(blank=True)),
                ('twitter', models.URLField(blank=True)),
                ('instagram', models.URLField(blank=True)),
                ('linkdin', models.URLField(blank=True)),
                ('memberbranch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Leader_app.branchyear')),
                ('namebranch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Leader_app.branchname')),
            ],
            options={
                'verbose_name_plural': 'Branch member',
                'ordering': ('id',),
            },
        ),
    ]