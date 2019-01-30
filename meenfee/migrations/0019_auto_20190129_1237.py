# Generated by Django 2.1.5 on 2019-01-29 12:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('meenfee', '0018_auto_20190127_1834'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience', models.TextField(blank=True, null=True)),
                ('levelskill', models.CharField(choices=[('Beginner', 'Beginner'), ('Medium', 'medium'), ('Expert', 'Expert')], max_length=120)),
                ('location', models.CharField(choices=[('I travel to my customers', 'I travel to my customers'), ('Customers travel to me', 'Customers travel to me'), ('Remotely', 'Remotely')], max_length=120)),
                ('distance_limit', models.CharField(choices=[('5 minutes away', '5 minutes away'), ('20 minutes away', '20 minutes away'), ('30 minutes away', '30 minutes away')], max_length=100)),
                ('service_pricing', models.PositiveIntegerField()),
                ('pricing_unit', models.CharField(max_length=30)),
                ('quote_at_request', models.BooleanField(default=False, help_text='This will create popup when they accept a requester request')),
                ('provide_tools', models.BooleanField(default=True)),
                ('tool_specify', models.TextField(blank=True, null=True)),
                ('instant_booking', models.BooleanField(default=True)),
                ('profile_pic', models.ImageField(default='service/img/default.jpg', upload_to='service/img')),
            ],
            options={
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.CreateModel(
            name='ServiceProviderAvailability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availability_date', models.DateField()),
                ('availability_time_from', models.TimeField()),
                ('availability_time_to', models.TimeField()),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meenfee.Service')),
            ],
            options={
                'verbose_name_plural': 'Service Provider Availability',
            },
        ),
        migrations.RemoveField(
            model_name='serviceprovider',
            name='category',
        ),
        migrations.RemoveField(
            model_name='serviceprovider',
            name='subCategory',
        ),
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='city',
            field=models.CharField(max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='subcategory',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='userotherinfo',
            name='usertype',
            field=models.CharField(blank=True, choices=[('provider', 'Provider'), ('requester', 'Requester')], max_length=20, null=True),
        ),
        migrations.DeleteModel(
            name='ServiceProvider',
        ),
        migrations.AddField(
            model_name='service',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meenfee.Category'),
        ),
        migrations.AddField(
            model_name='service',
            name='city',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='meenfee.City'),
        ),
        migrations.AddField(
            model_name='service',
            name='subcategory',
            field=models.ManyToManyField(to='meenfee.SubCategory'),
        ),
        migrations.AddField(
            model_name='service',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
