from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.base import Model


class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=512)
    bid = models.DecimalField(max_digits=10, decimal_places=2)
    num_bids = models.IntegerField(null=True)
    category = models.CharField(max_length=64, null=True)

class Bid(models.Model):
    bid_owner_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bid_owners")
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)

class Comment(models.Model):
    comment = models.CharField(max_length=512)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)