from django.urls import reverse_lazy
from .models import Post
from .forms import ArticleForm, UpdateForm
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

# Create your views here.


class HomepageView(ListView):
    model = Post
    template_name = 'blog/homepage.html'


class ArticleView(DetailView):
    model = Post
    template_name = 'blog/article.html'


class AddArticleView(CreateView):
    model = Post
    form_class = ArticleForm
    template_name = "blog/add_article.html"


class UpdateArticleView(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = "blog/update_article.html"


class DeleteArticleView(DeleteView):
    model = Post
    template_name = 'blog/delete_article.html'
    success_url = reverse_lazy('homepage')
