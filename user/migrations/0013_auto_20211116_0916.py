# Generated by Django 3.2.8 on 2021-11-16 01:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_auto_20211116_0849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 16, 9, 16, 16, 374503), verbose_name='Date '),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 16, 9, 16, 16, 374503), verbose_name='Date '),
        ),
    ]
