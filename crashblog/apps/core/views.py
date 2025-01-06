from django.shortcuts import render
from django.http import HttpResponse

from apps.blog.models import Post

# Create your views here.
def frontpage(request):
    posts = Post.objects.filter(status='published')
    return render(request, 'core/frontpage.html', {'posts': posts})

def about(request):
    return render(request, 'core/about.html')

def robots_txt(request):
    text=[
        "User-agent: *",
        "Disallow: /admin/",
    ]
    return HttpResponse("\n".join(text), content_type="text/plain")
