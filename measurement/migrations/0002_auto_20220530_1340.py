# Generated by Django 3.1.2 on 2022-05-30 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='measurement',
            options={'verbose_name': 'Измерение', 'verbose_name_plural': 'Измерения'},
        ),
    ]
