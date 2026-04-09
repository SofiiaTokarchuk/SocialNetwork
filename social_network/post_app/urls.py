from django. urls import path
from .views import render_my_posts

urlpatterns = [
    path('my-posts/', render_my_posts, name='my_posts')
]
