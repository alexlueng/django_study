from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views.generic import DetailView
# Create your views here.

User = get_user_model()

class ProfileDetailView(DetailView):
#	queryset = User.objects.filter(is_active=True)
	template_name = "profiles/user.html"
	def get_object(self):
		username = self.kwargs.get("username", None)
		if username is None:
			raise Http404
		return get_object_or_404(User, username__iexact=username, is_active=True)


