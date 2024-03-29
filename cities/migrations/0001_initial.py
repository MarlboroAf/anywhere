# Generated by Django 4.1.3 on 2022-11-25 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('city', models.TextField()),
                ('otherName', models.TextField()),
                ('country', models.TextField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('year', models.IntegerField()),
                ('pop', models.IntegerField()),
                ('city_id', models.TextField()),
            ],
        ),
    ]
