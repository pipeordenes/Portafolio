# Generated by Django 2.0.9 on 2020-09-11 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionTurismo', '0002_reserva'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transporte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descripcion', models.CharField(max_length=40)),
                ('Costo', models.IntegerField()),
            ],
        ),
    ]
