# Generated by Django 3.2.1 on 2021-05-14 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_rename_listing_owner_listing_listing_owner_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='num_bids',
            field=models.IntegerField(null=True),
        ),
    ]