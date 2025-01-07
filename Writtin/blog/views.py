from .models import Post
from .forms import ArticleForm
from django.views.generic import DetailView, ListView, CreateView

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
