from django.shortcuts import render
from .models import Post

# Create your views here.
def main(request):
    posts = Post.objects
    return render(request, 'crud/main.html', {'posts': posts})
