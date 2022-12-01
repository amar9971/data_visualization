from django import forms
from .models import Countrydata

class CountryDataForms(forms.ModelForm):
    class Meta:
        model = Countrydata
        fields= '__all__'