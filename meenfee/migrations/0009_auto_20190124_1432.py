# Generated by Django 2.1.5 on 2019-01-24 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meenfee', '0008_auto_20190124_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceprovider',
            name='bannerImage',
            field=models.ImageField(default='static/admin/img/img.jpg', upload_to='static/admin/img'),
        ),
    ]
