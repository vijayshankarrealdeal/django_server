# Generated by Django 4.0 on 2022-01-05 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fly', '0012_remove_bookflighttickets_flight_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookflighttickets',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
