# Generated by Django 3.2.8 on 2021-11-23 15:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0023_auto_20211123_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 23, 23, 38, 33, 174026), verbose_name='Date '),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 23, 23, 38, 33, 174026), verbose_name='Date '),
        ),
    ]