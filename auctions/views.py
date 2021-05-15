from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from .models import User, Listing, UsersListings


def index(request):
    # Build active listings list
    listings = Listing.objects.all()
    return render(request, "auctions/index.html", {
        "listings": listings    # listings is a list of all active listings
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def listing(request):
    if request.method == "GET" and request.GET.get("listing_title"):
        listing_title = request.GET.get("listing_title")
        listing_description = request.GET.get("listing_description")
        listing_bid = request.GET.get("listing_bid")
        listing_category = request.GET.get("listing_category")
        img_url = request.GET.get("img_url")
        # Save listing object
        l = Listing(title=listing_title, 
                    description=listing_description, 
                    bid=listing_bid, 
                    category=listing_category,
                    img_url=img_url)
        l.save()
        return HttpResponseRedirect(reverse("index"))
    return render(request, "auctions/listing.html")

def listing_view(response, listing_id):
    """
    Prepares listing view
    """
    listing = Listing.objects.get(id=listing_id)
    return render(response, "auctions/listing-view.html", {
        "listing": listing
    })
    pass

def admin_watchlist(response, user_id, action, listing_id):
    """
    Admins the watchlist
    """
    user = User.objects.get(id=user_id)
    listing = Listing.objects.get(id=listing_id)
    if action == "add":
        ul = UsersListings(user_id=user.id, listing_id=listing.id)
        # TODO: Add only if not present
        ul.save()
    watchlist(response, user_id)
    return HttpResponseRedirect(reverse('watchlist', args=(user_id,)))

def watchlist(response, user_id):
    user_listings = UsersListings.objects.filter(user_id=user_id)
    listings = []
    for users_listing in user_listings:
        listings.append(Listing.objects.get(id=users_listing.listing_id)) 
    return render(response, "auctions/watchlist.html", {
        "listings": listings
    })