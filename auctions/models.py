from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=512)
    price = models.DecimalField(decimal_places=2)
    num_bids = models.IntegerField()
    listing_owner = models.CharField(max_length=64)
    listing_category = models.CharField(max_length=64)

class Bid():
    pass

class AuctionComment():
    pass