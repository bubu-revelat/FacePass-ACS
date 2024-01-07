# Generated by Django 3.0.8 on 2020-07-28 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=16, null=True)),
                ('type', models.CharField(blank=True, max_length=128, null=True)),
                ('description', models.TextField()),
                ('amenities', models.TextField()),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
