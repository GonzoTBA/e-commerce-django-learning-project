# Generated by Django 3.2.1 on 2021-05-19 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_listing_owner_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='winner_id',
            field=models.IntegerField(null=True),
        ),
    ]
