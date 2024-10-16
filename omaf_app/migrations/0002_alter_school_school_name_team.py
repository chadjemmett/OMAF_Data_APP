# Generated by Django 5.1.2 on 2024-10-16 14:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('omaf_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='school_name',
            field=models.CharField(max_length=256, unique=True, verbose_name='School Name'),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=256, verbose_name='Team Name')),
                ('onsite_competition', models.BooleanField(default=True)),
                ('category', models.CharField(choices=[('bnp', 'Broadcast News Package'), ('ba', 'Broadcast Anchor'), ('pf', 'Photography Fashion'), ('pcr', 'Photograpy Creative'), ('pcm', 'Photography Commercial'), ('pst', 'Photography Street'), ('vre', 'Video Convention Recap'), ('vpsa', 'Video Public Service Announcment'), ('fftf', 'Film Finish the Film'), ('f3m', 'Film 3 Minutes'), ('f30', 'Film 30 Seconds'), ('sm', 'Social Media Instagram'), ('gd', 'Graphic Design, Digital'), ('pj', 'Print News Reporting'), ('pld', 'Print Publication Layout & Design')], max_length=256)),
                ('students', models.TextField(max_length=512)),
                ('place', models.CharField(blank=True, choices=[('1st', 'First Place'), ('2nd', 'Second Place'), ('3rd', 'Third Place')], max_length=256)),
                ('flash_drive', models.CharField(max_length=256, verbose_name='Flash Drive Size')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='omaf_app.school')),
            ],
        ),
    ]