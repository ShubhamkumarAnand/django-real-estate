from django.shortcuts import render
from . import models
from . import forms

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


def listing_create(request):
    form = forms.ListingForm
    context = {
        "form": form
    }
    return render(request, "listing_create.html", context)
