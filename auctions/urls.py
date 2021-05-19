from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("listing", views.listing, name="listing"),
    path("listing-view/<int:listing_id>", views.listing_view, name="listing-view"),
    path("admin_watchlist/<int:user_id>/<str:action>/<int:listing_id>", views.admin_watchlist, name="admin_watchlist"),
    path("watchlist/<int:user_id>", views.watchlist, name="watchlist"),
    path("close/<int:listing_id>/<int:highest_bidder_id>", views.close, name="close"),
    path("add_comment", views.add_comment, name="add_comment"),
    path("categories", views.categories, name="categories"),
    path("category/<str:category>", views.show_category, name="category"),
]
