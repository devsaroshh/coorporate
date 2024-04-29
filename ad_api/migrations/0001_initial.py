# Generated by Django 5.0.4 on 2024-04-29 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_type', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('ads_run', models.IntegerField()),
                ('spend', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
