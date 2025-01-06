from django.urls import path
from .views import post_detail,category_detail,search

app_name = 'blog'

urlpatterns = [
    path('search/', search, name='search'),
    path('<slug:slug>/', post_detail, name='post_detail'),
    path('category/<slug:slug>/', category_detail, name='category_detail'),
]
