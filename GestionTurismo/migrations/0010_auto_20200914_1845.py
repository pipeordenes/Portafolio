# Generated by Django 2.0.9 on 2020-09-14 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionTurismo', '0009_auto_20200914_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicioextra',
            name='Valor',
            field=models.IntegerField(),
        ),
    ]
