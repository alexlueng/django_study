from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView

from .models import RestaurantLocation
from .forms import RestaurantCreateForm, RestaurantLocationCreateForm

# Create your views here.



# class HomeView(TemplateView):
#   template_name = 'home.html'

#   def get_context_data(self, *args, **kwargs):
#     context = super(HomeView, self).get_context_data(*args, **kwargs)
#     context = {
#       "html_var": "alexlueng"
#     }
#     return context

# def restaurant_listview(request):
#   template_name = 'restaurants/restaurant_list.html'
#   queryset = RestaurantLocation.objects.all()
#   context = {
#     "object_list": queryset
#   }
#   return render(request, template_name, context)


class RestaurantListView(LoginRequiredMixin, ListView):
  # queryset = RestaurantLocation.objects.all()
 # template_name = 'restaurants/restaurant_list.html'

  # def get_queryset(self):
  #   print(self.kwargs)
  #   slug = self.kwargs.get("slug")
  #   if slug:
  #     queryset = RestaurantLocation.objects.filter(location__iexact=slug)
  #   else:
  #     queryset = RestaurantLocation.objects.all()
  #   return queryset
  def get_queryset(self):
    return RestaurantLocation.objects.filter(owner=self.request.user)

class RestaurantDetailView(LoginRequiredMixin, DetailView):
  def get_queryset(self):
    return RestaurantLocation.objects.filter(owner=self.request.user)

  # def get_context_data(self, *args, **kwargs):
  #   print(self.kwargs)
  #   context = super(RestaurantDetailView, self).get_context_data(*args, **kwargs)
  #   print(context)
  #   return context

  # def get_object(self, *args, **kwargs):
  #   rest_id = self.kwargs.get("rest_id")
  #   obj = get_object_or_404(RestaurantLocation, id=rest_id)
  #   return obj


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

# def restaurant_createview(request):
#   # if request.method == 'GET':
#   #   print("get data")
#   form = RestaurantCreateForm(request.POST or None)
#   errors = None
#     # if request.method == 'POST':
#     # print("post data")
#     # title = request.POST.get('title')
#     # location = request.POST.get('location')
#     # category = request.POST.get('category')
#     # form = RestaurantCreateForm(request.POST)
#   if form.is_valid():
#     obj = RestaurantLocation.objects.create(
#       name = form.cleaned_data.get('name'),
#       location = form.cleaned_data.get('location'),
#       category = form.cleaned_data.get('category')
#     )
#     return HttpResponseRedirect("/restaurants/")
#   if form.errors:
#     errors =form.errors
#   template_name = 'restaurants/form.html'
#   context = {"form": form, "errors": errors}
#   return render(request, template_name, context)

# @login_required(login_url='/login/')
# def restaurant_createview(request):
#   form = RestaurantLocationCreateForm(request.POST or None)
#   errors = None
#   if form.is_valid():
#     if request.user.is_authenticated():
#       instance = form.save(commit=False)
#       instance.owner = request.user
#       form.save()
#       return HttpResponseRedirect("/restaurants/")
#     else:
#       return HttpResponseRedirect("/login/")
#   if form.errors:
#     errors = form.errors
#   template_name = 'restaurants/form.html'
#   context = {"form": form, "errors": errors}
#   return render(request, template_name, context)


class RestaurantCreateView(LoginRequiredMixin, CreateView):
  form_class = RestaurantLocationCreateForm
  template_name = "form.html"
  # success_url = "/restaurants/"
  login_url = '/login'

  def form_valid(self, form):
    instance = form.save(commit=False)
    instance.owner = self.request.user
    # instance.save()
    return super(RestaurantCreateView, self).form_valid(form)

  def get_context_data(self, *args, **kwargs):
    context = super(RestaurantCreateView, self).get_context_data(*args, **kwargs)
    context['title'] ='Add Restaurant'
    return context

class RestaurantUpdateView(LoginRequiredMixin, UpdateView):
  form_class = RestaurantLocationCreateForm
  template_name = "form.html"
  # success_url = "/restaurants/"
  login_url = '/login'

  def get_context_data(self, *args, **kwargs):
    context = super(RestaurantUpdateView, self).get_context_data(*args, **kwargs)
    context['title'] ='Update Restaurant'
    return context
    
  def get_queryset(self):
    return RestaurantLocation.objects.filter(owner=self.request.user)

