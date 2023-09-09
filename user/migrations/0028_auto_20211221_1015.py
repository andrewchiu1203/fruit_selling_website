# Generated by Django 3.2.9 on 2021-12-21 02:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0027_auto_20211124_0011'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='timezone',
            field=models.CharField(default='UTC +0', max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='time_created',
            field=models.CharField(default='2021-12-21 10:15:30.387220', max_length=20),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 21, 10, 15, 30, 387220), verbose_name='Date '),
        ),
    ]
