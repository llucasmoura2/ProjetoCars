# Generated by Django 5.0.3 on 2024-05-09 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0010_alter_car_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='value',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
