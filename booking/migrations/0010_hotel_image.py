# Generated by Django 3.0.8 on 2020-08-02 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0009_auto_20200731_0323'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='hotel_pic'),
        ),
    ]
