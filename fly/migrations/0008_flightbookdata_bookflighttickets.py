# Generated by Django 4.0 on 2022-01-03 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('fly', '0007_postfood_prefood'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlightBookData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_image', models.CharField(max_length=70)),
                ('fight_name', models.CharField(max_length=70)),
                ('flight_no', models.CharField(max_length=70)),
                ('origin_time', models.CharField(max_length=70)),
                ('origin_place', models.CharField(max_length=70)),
                ('destination_time', models.CharField(max_length=70)),
                ('destination_place', models.CharField(max_length=70)),
                ('duration_stop', models.CharField(max_length=70)),
                ('no_stops', models.CharField(max_length=70)),
                ('price', models.CharField(max_length=70)),
                ('refund', models.CharField(max_length=70)),
                ('total_pay', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='BookFlightTickets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardNumber', models.CharField(max_length=30)),
                ('cardMonth', models.CharField(max_length=30)),
                ('cardYear', models.CharField(max_length=30)),
                ('cardType', models.CharField(max_length=30)),
                ('cardCvv', models.CharField(max_length=30)),
                ('flight', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='fly.flightbookdata')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]