# Generated by Django 2.1.5 on 2019-02-01 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meenfee', '0027_livebooking_requester'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompletedBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirmed_by_requester', models.BooleanField(default=False)),
                ('confirmed_by_provider', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Completed Booking',
            },
        ),
        migrations.AlterModelOptions(
            name='notification',
            options={'verbose_name_plural': 'Notification'},
        ),
        migrations.AlterModelOptions(
            name='rowbooking',
            options={'verbose_name': 'Booking', 'verbose_name_plural': 'Bookings'},
        ),
        migrations.AlterField(
            model_name='livebooking',
            name='booking_status',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='completedbooking',
            name='rowbooking_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='meenfee.RowBooking'),
        ),
    ]
