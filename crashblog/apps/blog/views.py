from django.shortcuts import render, get_object_or_404,redirect
from .models import Post,Category
from .forms import CommentForm

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status='published')
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect('blog:post_detail', slug=slug)
    else:
        form = CommentForm()
    
    return render(request, 'blog/post_detail.html', {'post': post, 'form': form})

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts_set.filter(status='published')
    return render(request, 'blog/category_detail.html', {'category': category})

def search(request):
    query = request.GET.get('query')
    posts = Post.objects.filter(title__icontains=query)
    return render(request, 'blog/search.html', {'posts': posts, 'query': query})