# Generated by Django 5.0.3 on 2024-05-20 13:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0012_car_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='car_brand', to='cars.brand'),
        ),
    ]
