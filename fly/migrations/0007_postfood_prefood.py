# Generated by Django 4.0 on 2021-12-31 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fly', '0006_alter_shopsinternational_contanct_details_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostFood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=2500)),
                ('title', models.CharField(max_length=2500)),
                ('content', models.CharField(max_length=2500)),
                ('opening', models.CharField(max_length=2500)),
                ('location', models.CharField(max_length=2500)),
                ('contanct_details', models.CharField(max_length=2500)),
            ],
        ),
        migrations.CreateModel(
            name='PreFood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=2500)),
                ('title', models.CharField(max_length=2500)),
                ('content', models.CharField(max_length=2500)),
                ('opening', models.CharField(max_length=2500)),
                ('location', models.CharField(max_length=2500)),
                ('contanct_details', models.CharField(max_length=2500)),
            ],
        ),
    ]
