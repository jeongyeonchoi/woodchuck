from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def main(request):
    posts = Post.objects
    return render(request, 'crud/main.html', {'posts': posts})

def show(request, post_id):
    post = get_object_or_404(Post, pk = post_id )
    return render(request, 'crud/show.html', {'post': post})