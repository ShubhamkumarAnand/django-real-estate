from django.forms import ModelForm
from . import models


class ListingForm(ModelForm):
    class Meta:
        model = models.Listing
        fields = [
            "title",
            "price",
            "num_bedrooms",
            "num_bathrooms",
            "square_footage",
            "address",
            "image"
        ]
