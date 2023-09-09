# Generated by Django 3.2.8 on 2021-11-16 00:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '__first__'),
        ('user', '0010_auto_20211116_0810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 16, 8, 48, 44, 894340), verbose_name='Date '),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 16, 8, 48, 44, 894340), verbose_name='Date '),
        ),
    ]
