# Generated by Django 3.2.5 on 2021-11-21 08:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20211121_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 21, 8, 58, 42, 398918, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 21, 8, 58, 42, 394865, tzinfo=utc)),
        ),
    ]
