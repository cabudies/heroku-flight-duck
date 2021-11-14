# Generated by Django 2.2 on 2021-11-13 21:39

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AutoSuggestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='BrowseRouteModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(max_length=10)),
                ('destination', models.CharField(max_length=10)),
                ('departureDate', models.CharField(max_length=100)),
                ('returnDate', models.CharField(blank=True, max_length=100)),
                ('currency_format', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='CityModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(default='', max_length=200)),
                ('city_code', models.CharField(default='', max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CountryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CurrencyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('symbol', models.CharField(max_length=1000)),
                ('thousands_separator', models.CharField(max_length=2)),
                ('decimal_separator', models.CharField(max_length=2)),
                ('symbol_on_left', models.BooleanField(default=True)),
                ('space_between_amount_and_symbol', models.BooleanField(default=True)),
                ('rounding_coefficient', models.IntegerField(default=0)),
                ('decimal_digits', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='FlightsHotelPackageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('originplace', models.CharField(max_length=10)),
                ('destinationplace', models.CharField(max_length=10)),
                ('outbounddate', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Length has to be 10', regex='^.{10}$')])),
                ('inbounddate', models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(message='Length has to be 10', regex='^.{10}$')])),
                ('adults', models.IntegerField(default=0)),
                ('rooms', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1)])),
                ('children', models.IntegerField(blank=True, default=0)),
                ('infants', models.IntegerField(blank=True, default=0)),
                ('country', models.CharField(max_length=10)),
                ('currency_format', models.CharField(max_length=10)),
                ('destination_code', models.CharField(blank=True, default='', max_length=10)),
                ('locale', models.CharField(max_length=10)),
                ('trip_days', models.IntegerField(blank=True, default=1, validators=[django.core.validators.MaxValueValidator(30)])),
                ('number_of_extended_months', models.IntegerField(blank=True, default=0, validators=[django.core.validators.MaxValueValidator(2)])),
                ('user_id', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FlightsLiveModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('originplace', models.CharField(max_length=10)),
                ('destinationplace', models.CharField(max_length=10)),
                ('outbounddate', models.CharField(max_length=100)),
                ('inbounddate', models.CharField(blank=True, max_length=100)),
                ('adults', models.IntegerField(default=0)),
                ('children', models.IntegerField(blank=True, default=0)),
                ('infants', models.IntegerField(blank=True, default=0)),
                ('country', models.CharField(max_length=100)),
                ('currency', models.CharField(max_length=100)),
                ('locale', models.CharField(max_length=100)),
                ('user_id', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LocaleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='AirportModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airport_name', models.CharField(max_length=200)),
                ('airport_code', models.CharField(max_length=20)),
                ('city', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='flights.CityModel')),
                ('country', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='flights.CountryModel')),
            ],
        ),
    ]