from django.shortcuts import render, get_object_or_404,redirect
from .models import Post
from .forms import CommentForm

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect('blog:post_detail', slug=slug)
    else:
        form = CommentForm()
    
    return render(request, 'blog/detail.html', {'post': post, 'form': form})
