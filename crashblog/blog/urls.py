from django.urls import path
from .views import post_detail,category_detail

app_name = 'blog'

urlpatterns = [
    path('<slug:slug>/', post_detail, name='post_detail'),
    path('category/<slug:slug>/', category_detail, name='category_detail'),
]
