from django.urls import reverse_lazy
from .models import Post
from .forms import PostCreateForm, PostUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    DetailView, ListView, CreateView,
    UpdateView, DeleteView
)


class PostListView(ListView):
    login_url = "login"
    redirect_field_name = "login"
    model = Post
    template_name = "blog/all_posts.html"
    context_object_name = "blog_posts"
    ordering = ['-created_at']


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_details.html"


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = "blog/create_post.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostEditView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostUpdateForm
    template_name = "blog/edit_post.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "blog/delete_post.html"
    success_url = reverse_lazy('all_posts')

    def form_valid(self, form):
        return super().form_valid(form)
