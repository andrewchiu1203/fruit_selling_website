# Generated by Django 3.2.9 on 2021-12-21 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0030_auto_20211221_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='time_created',
            field=models.CharField(default='伺服器時間: 2021-12-22 00:17:35.086926', max_length=32),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='last_modified',
            field=models.CharField(default='2021-12-22 00:17:35', max_length=32),
        ),
    ]
