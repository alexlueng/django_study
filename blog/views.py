from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post
from .forms import PostForm
# Create your views here.
def post_detail(request, id=None):
	instance = get_object_or_404(Post, id=id)
	context = {
		'title': instance.title,
		'instance': instance
	}
	template_name = 'blog/detail.html'
	return render(request, template_name, context)

def post_list(request):
	queryset_list = Post.objects.all().order_by("-timestamp")
	paginator = Paginator(queryset_list, 3)

	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
      # If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
      # If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)

	context = {
		'obj': queryset
	}
	template_name = 'blog/list.html'
	return render(request, template_name, context)

def post_create(request):
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		# messages.success(request, "Successfully created.")
		return HttpResponseRedirect(instance.get_absolute_url())
	# else:
	# 	messages.error(request, "Failed created.")
	context = {
		'form': form
	}
	template_name = 'blog/create.html'
	# if request.method == 'POST':
	# 	print(request.POST.get('title'))
	return render(request, template_name, context)

def post_update(request, id=None):
	template_name = 'blog/create.html'
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		# messages.success(request, "Successfully updated.")
		return HttpResponseRedirect(instance.get_absolute_url())
	# else:
	# 	messages.error(request, "Failed updated.")
	context = {
		'instance': instance,
		'form': form
	}
	return render(request, template_name, context)

def post_delete(request, id=id):
	instance = get_object_or_404(Post, id=id)
	instance.delete()
	return redirect("blog:list")
