from django.urls import path
from .views import post_detail

app_name = 'blog'

urlpatterns = [
    path('<slug:slug>/', post_detail, name='post_detail'),
]
