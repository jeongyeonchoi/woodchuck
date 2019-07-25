from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

# Create your views here.
def main(request):
    posts = Post.objects
    return render(request, 'crud/main.html', {'posts': posts})

def show(request, post_id):
    post = get_object_or_404(Post, pk = post_id )
    return render(request, 'crud/show.html', {'post': post})

def new(request):
    return render(request, 'crud/new.html')

def postcreate(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('main')
    else:
        form = PostForm()
        return render(request, 'crud/new.html', {'form': form})

def edit(request):
    return render(request, 'crud/edit.html')

def postupdate(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('show', post_id=post.pk)
    else:
        form = PostForm(instance=post)
        return render(request, 'crud/edit.html', {'form': form})

def postdelete(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    post.delete()
    return redirect('main')