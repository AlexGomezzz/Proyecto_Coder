# Generated by Django 4.0.3 on 2022-04-06 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcoder', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hijos',
            name='id',
        ),
        migrations.RemoveField(
            model_name='padres',
            name='id',
        ),
        migrations.AlterField(
            model_name='hijos',
            name='ci',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='padres',
            name='ci',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]