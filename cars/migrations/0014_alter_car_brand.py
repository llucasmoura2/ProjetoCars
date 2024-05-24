# Generated by Django 5.0.3 on 2024-05-20 14:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0013_alter_car_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.ForeignKey(blank=True, max_length=30, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='car_brand', to='cars.brand'),
        ),
    ]
