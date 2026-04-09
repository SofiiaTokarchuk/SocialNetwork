from django. urls import path
from .views import render_settings

urlpatterns = [
    path('settings/', render_settings, name='my_posts')
]
