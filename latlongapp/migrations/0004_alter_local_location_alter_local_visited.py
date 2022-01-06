# Generated by Django 4.0.1 on 2022-01-06 16:29

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('latlongapp', '0003_alter_local_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='local',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(null=True, srid=4326),
        ),
        migrations.AlterField(
            model_name='local',
            name='visited',
            field=models.DateTimeField(null=True),
        ),
    ]