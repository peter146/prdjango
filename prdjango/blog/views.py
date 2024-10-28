from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts}) #if the dictionary with the posts variable is missing, no posts will be displayed!

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_inhoud.html', {'post': post})

    # try:
    #     post = get_object_or_404(Post, pk=pk)
    # except Post.DoesNotExist: 
    #     print(f'Post with PK {pk} does not exist.')
    # return render(request, 'blog/post_inhoud.html', {'post': post})