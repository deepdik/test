# Generated by Django 2.1.5 on 2019-02-01 04:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meenfee', '0023_remove_rowbooking_provider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='canceledbooking',
            name='rowbooking_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='meenfee.RowBooking'),
        ),
    ]
