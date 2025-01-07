from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from apps.blog.models import Post,Category

class CategorySitemap(Sitemap):
    def items(self):
        return Category.objects.all()
    
class PostSitemap(Sitemap):
    def items(self):
        return Post.objects.filter(status='published')
    def lastmod(self, obj):
        return obj.created_at

