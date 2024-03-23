# Generated by Django 5.0.3 on 2024-03-23 14:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='currencydata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=120)),
                ('country_code', models.CharField(max_length=5)),
                ('country_currency_value', models.DecimalField(decimal_places=20, max_digits=25)),
                ('currency_update_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
