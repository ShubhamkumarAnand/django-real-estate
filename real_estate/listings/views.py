from django.shortcuts import render
from . import models

# Create your views here.


def listing_list(request):
    listings = models.Listing.objects.all()
    context = {
        "listings": listings
    }
    return render(request, "listings.html", context)


def listing_retrieve(request, pk):
    listing = models.Listing.objects.get(id=pk)
    context = {
        "listing": listing
    }
    return render(request, "listing.html", context)
