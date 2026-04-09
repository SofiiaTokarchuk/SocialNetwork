from django.shortcuts import render

# Create your views here.

def render_my_posts(request):
    return render(request, 'my_posts.html')