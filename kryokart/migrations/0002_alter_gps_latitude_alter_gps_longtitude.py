# Generated by Django 4.0.3 on 2022-04-19 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kryokart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gps',
            name='latitude',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='gps',
            name='longtitude',
            field=models.CharField(max_length=15),
        ),
    ]
