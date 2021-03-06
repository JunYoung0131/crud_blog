from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone

def home(request):
    blogs = Blog.objects.all() 
    return render(request, 'home.html', {'blogs':blogs})

def detail(request, id):
    blog = get_object_or_404(Blog, pk=id)
    return render(request, 'detail.html', {'blog':blog})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.write = request.POST['write']
    new_blog.body = request.POST['body']
    new_blog.pud_date = timezone.now()
    new_blog.save()
    return redirect('home')

def edit(request, id):
    edit_blog = get_object_or_404(Blog, pk=id)
    return render(request, 'edit.html', {'blog':edit_blog})

def update(request, id):
    update_blog = get_object_or_404(Blog, pk=id)
    update_blog.title = request.POST['title']
    update_blog.write = request.POST['write']
    update_blog.body = request.POST['body']
    update_blog.pud_date = timezone.now()
    update_blog.save()
    return redirect('home')

def delete(request, id):
    delete_blog = get_object_or_404(Blog, pk=id)
    delete_blog.delete()
    return redirect('home')