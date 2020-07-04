# Generated by Django 3.0.8 on 2020-07-04 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_packages', '0002_auto_20200704_2240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tourpackages',
            name='destinations',
        ),
        migrations.AddField(
            model_name='tourpackages',
            name='destinations',
            field=models.ManyToManyField(to='travel_packages.Destinations'),
        ),
    ]