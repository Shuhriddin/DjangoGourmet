from django import forms
from .models import FoodApp


class CreateFood(forms.ModelForm):
    class Meta:
        model = FoodApp
        fields = ['name_food', 'type_food', 'price_food', 'image_food', 'description_food']