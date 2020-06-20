from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post

def all_posts(request):
	posts = Post.objects.all().order_by('-date') # Order by most recent
	paginator = Paginator(posts, 7)
	page = request.GET.get('page')
	posts = paginator.get_page(page)
	return render(request, 'blog/all_posts.html', {'posts': posts})

def detail(request, post_id):
	post = get_object_or_404(Post, pk=post_id) # pk => primary key
	return render(request, 'blog/detail.html', {'post': post})