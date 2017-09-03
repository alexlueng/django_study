from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from .models import RestaurantLocation

# Create your views here.



# class HomeView(TemplateView):
#   template_name = 'home.html'

#   def get_context_data(self, *args, **kwargs):
#     context = super(HomeView, self).get_context_data(*args, **kwargs)
#     context = {
#       "html_var": "alexlueng"
#     }
#     return context

def restaurant_listview(request):
  template_name = 'restaurants/restaurant_list.html'
  queryset = RestaurantLocation.objects.all()
  context = {
    "object_list": queryset
  }
  return render(request, template_name, context)


class RestaurantListView(ListView):
  # queryset = RestaurantLocation.objects.all()
 # template_name = 'restaurants/restaurant_list.html'

  def get_queryset(self):
    print(self.kwargs)
    slug = self.kwargs.get("slug")
    if slug:
      queryset = RestaurantLocation.objects.filter(location__iexact=slug)
    else:
      queryset = RestaurantLocation.objects.all()
    return queryset

class RestaurantDetailView(DetailView):
  queryset = RestaurantLocation.objects.all()

  def get_context_data(self, *args, **kwargs):
    print(self.kwargs)
    context = super(RestaurantDetailView, self).get_context_data(*args, **kwargs)
    print(context)
    return context

  def get_object(self, *args, **kwargs):
    rest_id = self.kwargs.get("rest_id")
    obj = get_object_or_404(RestaurantLocation, id=rest_id)
    return obj


# class SearchRestaurantListView(ListView):

#   template_name = 'restaurants/restaurant_list.html'

#   def get_queryset(self):
#     print(self.kwargs)
#     slug = self.kwargs.get("slug")
#     if slug:
#       queryset = RestaurantLocation.objects.filter(location__iexact=slug)
#     else:
#       queryset = RestaurantLocation.objects.none()
#     return queryset

# class YangjiangRestaurantListView(ListView):
#   queryset = RestaurantLocation.objects.filter(location__iexact='yangjiang')
#   template_name = 'restaurants/restaurant_list.html'
