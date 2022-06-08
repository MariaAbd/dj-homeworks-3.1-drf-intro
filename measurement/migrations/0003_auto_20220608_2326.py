# Generated by Django 3.1.2 on 2022-06-08 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_auto_20220530_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='sensor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='measurements', to='measurement.sensor', verbose_name='Название датчика'),
        ),
    ]
