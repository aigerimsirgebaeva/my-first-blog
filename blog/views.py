from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
    Post.objects.get(pk=pk)
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
#request - берет запрос
#render - делает шаблон
#'blog/post_list.html' - template file
#{} - is a place in which we can add some things for the template to use
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid(): #to check if the form is correct
            post = form.save(commit=False) #we save the form #commit=False means that we don't want to save the Post model yet – we want to add the author first
            post.author = request.user
            post.published_date = timezone.now()
            post.save() #will preserve changes (adding the author)
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm() #If method is POST then we want to construct the PostForm with data from the form
    return render(request, 'blog/post_edit.html', {'form': form}) #go to the post_detail page for the newly created post"
    #post_detail is the name of the view we want to go to
    #to pass it to the views, we use pk=post.pk, where post is the newly created blog post
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})