from django.shortcuts import render
from .models import Post
from django.views.generic import DetailView, ListView

# Create your views here.


class HomepageView(ListView):
    model = Post
    template_name = 'blog/homepage.html'


class ArticleView(DetailView):
    model = Post
    template_name = 'blog/article.html'
