# Generated by Django 3.2.8 on 2021-11-16 00:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_auto_20211116_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 16, 8, 49, 17, 392936), verbose_name='Date '),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 16, 8, 49, 17, 392936), verbose_name='Date '),
        ),
    ]