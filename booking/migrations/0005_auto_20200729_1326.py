# Generated by Django 3.0.8 on 2020-07-29 13:26

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking', '0004_auto_20200729_1325'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bokking',
            new_name='Booking',
        ),
    ]
