from django.shortcuts import render,HttpResponse
from Blog.models import Post
# Create your views here.

def bloghome(requests):
    allPosts=Post.objects.all()
    context={'allPosts':allPosts}
    return render(requests,'blog/bloghome.html',context)


def blogPost(requests,slug):
    post=Post.objects.filter(slug=slug).first()
    context={'post':post}
    return render(requests,'blog/blogPost.html',context)


