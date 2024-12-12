# Generated by Django 5.1.2 on 2024-12-06 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('omaf_app', '0005_alter_team_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='place',
            field=models.CharField(blank=True, choices=[('1st', 'First Place'), ('2nd', 'Second Place'), ('3rd', 'Third Place')], max_length=256),
        ),
    ]