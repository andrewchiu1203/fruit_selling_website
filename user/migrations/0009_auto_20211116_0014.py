# Generated by Django 3.2.8 on 2021-11-15 16:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20211115_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 16, 0, 14, 31, 892691), verbose_name='Date '),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 16, 0, 14, 31, 892691), verbose_name='Date '),
        ),
    ]
