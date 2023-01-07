from django.shortcuts import render, redirect
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
    form = forms.ListingForm()
    if request.method == 'POST':
        form = forms.ListingForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        "form": form
    }
    return render(request, "listing_create.html", context)


def listing_update(request, pk):
    listing = models.Listing.objects.get(id=pk)
    form = forms.ListingForm(instance=listing)
    if request.method == 'POST':
        form = forms.ListingForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        "form": form
    }
    return render(request, "listing_update.html", context)
