# Generated by Django 2.1.5 on 2019-02-01 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meenfee', '0025_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livebooking',
            name='rowbooking_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='meenfee.RowBooking'),
        ),
    ]