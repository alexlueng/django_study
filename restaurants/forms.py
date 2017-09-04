from django import forms
from .models import RestaurantLocation
#from django.forms import ModelForm

class RestaurantCreateForm(forms.Form):
  name = forms.CharField()
  location = forms.CharField(required=False)
  category = forms.CharField(required=False)

class RestaurantLocationCreateForm(forms.ModelForm):
  class Meta:
  	model = RestaurantLocation
  	fields = [
  	  'name',
  	  'location',
  	  'category',
  	]