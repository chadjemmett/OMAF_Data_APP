# Generated by Django 5.1.2 on 2024-10-17 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('omaf_app', '0002_alter_school_school_name_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=256, verbose_name='Last Name')),
            ],
        ),
    ]
