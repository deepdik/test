# Generated by Django 2.1.5 on 2019-01-27 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meenfee', '0017_auto_20190127_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userotherinfo',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='userotherinfo',
            name='usertype',
            field=models.CharField(blank=True, choices=[('1', 'Provider'), ('2', 'Requester')], max_length=20, null=True),
        ),
    ]
