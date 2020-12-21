from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from .models import Post


# Create your views here


def first(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'posts/first.html', context)


def main(request, post_id):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            return render('/thanks/')
    else:
        form = PostForm()
        return render('contact.html', {'form': form})

    post = get_object_or_404(Post, pk=post_id)
    default_like_count = post.like_count
    post.like_count = default_like_count + 1

    n = len(form)
    for i in range(0, n - 1):
        max = i
        for j in range(i + 1, n):
            if form[j] > form[max]:
                max = j
        form[i], form[max] = form[max], form[i]
    return render(request, 'posts/main.html')


def new(request):

    form = PostForm()
    return render(request, 'posts/main.html', {'form': form})


def a(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    default_view_count = post.view_count
    post.view_count = default_view_count + 1
    post.save()
    context = {
        'post': post
    }
    return render(request, 'posts/show.html', context)