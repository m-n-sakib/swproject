# Generated by Django 4.1.5 on 2023-01-26 00:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("travello", "0018_alter_transactions_date_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transactions",
            name="Date_Time",
            field=models.CharField(
                default=datetime.datetime(
                    2023, 1, 26, 0, 4, 53, 50458, tzinfo=datetime.timezone.utc
                ),
                max_length=19,
            ),
        ),
    ]
