# Generated by Django 3.2.4 on 2021-06-13 11:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0008_auto_20210613_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='expiry_date',
            field=models.DateField(default=datetime.datetime(2048, 10, 29, 17, 24, 17, 55599)),
        ),
    ]