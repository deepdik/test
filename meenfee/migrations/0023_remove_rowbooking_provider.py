# Generated by Django 2.1.5 on 2019-01-31 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meenfee', '0022_auto_20190131_1705'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rowbooking',
            name='provider',
        ),
    ]
