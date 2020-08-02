# Generated by Django 3.0.8 on 2020-07-29 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_auto_20200729_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='no_of_guest',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='price',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
