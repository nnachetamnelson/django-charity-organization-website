from django.shortcuts import render
from .models import Events, Blog
from .models import Post, Author, PostView
from django.db.models import Count, Q
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import CommentForm, PostForm
from .models import Post, Author, PostView


def index(request):

    featured = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-timestamp')[0:3]

    if request.method == "POST":
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()


    context = {
        'object_list': featured,
        'latest': latest
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def donate(request):
    return render(request, 'donate.html')


def volunteer(request):
    return render(request, 'volunteer.html')


def contact(request):
    return render(request, 'contact.html')

def event(request):
    most_recent = Post.objects.order_by('-timestamp')[:3]
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'queryset': paginated_queryset,
        'most_recent': most_recent,
        'page_request_var': page_request_var,
    }
    return render(request, 'event.html', context)

def event_detailled(request, id):
    post = get_object_or_404(Post, id=id)
    context = {
        'post': post,
    }
    return render(request,'event_detail.html', context)
