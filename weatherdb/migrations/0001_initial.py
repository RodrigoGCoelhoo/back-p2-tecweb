# Generated by Django 3.2.7 on 2021-11-08 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityWeather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cidade', models.CharField(max_length=100)),
                ('lat', models.CharField(max_length=10)),
                ('long', models.CharField(max_length=10)),
            ],
        ),
    ]