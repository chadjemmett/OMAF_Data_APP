# Generated by Django 5.1.2 on 2024-10-29 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('omaf_app', '0002_remove_team_school_remove_team_students_team_advisor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='principal',
            field=models.CharField(max_length=256, verbose_name='Principal Name'),
        ),
    ]
