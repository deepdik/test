# Generated by Django 2.1.5 on 2019-01-29 18:48

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('meenfee', '0019_auto_20190129_1237'),
    ]

    operations = [
        migrations.CreateModel(
            name='CanceledBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cancel_date', models.DateTimeField(auto_now_add=True)),
                ('canceled_by', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Payment Methods',
            },
        ),
        migrations.CreateModel(
            name='LiveBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_status', models.CharField(blank=True, max_length=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_on_card', models.CharField(max_length=40)),
                ('card_num', models.CharField(max_length=15)),
                ('card_cvv', models.CharField(max_length=5)),
                ('card_exp', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Payment Methods',
            },
        ),
        migrations.CreateModel(
            name='ReScheduledAppointments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('re_scheduled_date', models.DateTimeField(auto_now_add=True)),
                ('confirmed_by_opp', models.BooleanField(default=False)),
                ('confirmed_by_opp_date', models.DateTimeField(blank=True, null=True)),
                ('re_scheduled_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Re-Scheduled Appointments',
            },
        ),
        migrations.CreateModel(
            name='RowBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_venue', models.CharField(blank=True, choices=[('Come to my place', 'Requester place'), ('Service provider place', 'Provider place'), ('Remotely', 'Remotely')], max_length=120, null=True)),
                ('appointment_gio_location', models.CharField(blank=True, max_length=30, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('appointment_date', models.DateField()),
                ('appointment_time_from', models.TimeField()),
                ('appointment_time_to', models.TimeField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('isacceptedbyprovider', models.BooleanField(default=False, help_text='accepted by provider on time')),
                ('isacceptedbyprovider_exp', models.BooleanField(default=False, help_text='accepted by provider after 5 min')),
                ('accepted_time', models.DateTimeField(blank=True, null=True)),
                ('ispaymentadd', models.BooleanField(default=False)),
                ('paymentaddtime', models.DateTimeField(blank=True, null=True)),
                ('appointment_city', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='meenfee.City')),
                ('requester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceFeedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='service',
            old_name='profile_pic',
            new_name='profile_img',
        ),
        migrations.AddField(
            model_name='service',
            name='avg_rating',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='service',
            name='completed_task',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='service',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='profile_views',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='service',
            name='response_within',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='type_of_tasker',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='servicerating',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meenfee.Service'),
        ),
        migrations.AddField(
            model_name='servicerating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='servicefeedback',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meenfee.Service'),
        ),
        migrations.AddField(
            model_name='servicefeedback',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rowbooking',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meenfee.Service'),
        ),
        migrations.AddField(
            model_name='rescheduledappointments',
            name='rowbooking_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='meenfee.RowBooking'),
        ),
        migrations.AddField(
            model_name='paymentmethod',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='meenfee.RowBooking'),
        ),
        migrations.AddField(
            model_name='paymentmethod',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='livebooking',
            name='booking_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='meenfee.RowBooking'),
        ),
        migrations.AddField(
            model_name='canceledbooking',
            name='rowbooking_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='meenfee.RowBooking'),
        ),
    ]