# Generated by Django 4.0.1 on 2022-01-04 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('latlongapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='local',
            name='iso2',
        ),
        migrations.RemoveField(
            model_name='local',
            name='iso3',
        ),
        migrations.RemoveField(
            model_name='local',
            name='mpoly',
        ),
        migrations.RemoveField(
            model_name='local',
            name='subregion',
        ),
        migrations.AlterField(
            model_name='local',
            name='region',
            field=models.CharField(max_length=100),
        ),
    ]
