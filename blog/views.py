from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm


# Create your views here.
def post_list(request):
	posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')
	return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk): #pk = číslo z adresy
	post = get_object_or_404(Post, pk=pk)
	return render(request,
		'blog/post_detail.html', {'post' : post})


def post_new(request):
	if request.method =="POST":
		form= PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit = False)
			post.author = request.user
			post.publish_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk) #pk = primary key - identifikátor příspěvku

	form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})

