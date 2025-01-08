from django.urls import path
from .views import *

urlpatterns = [
    path("", PostListView.as_view(), name="all_posts"),
    path("post/<int:pk>", PostDetailView.as_view(), name="post_detail"),
    path("create_post/", PostCreateView.as_view(), name="create_post"),
    path("edit_post/<int:pk>", PostEditView.as_view(), name="edit_post"),
    path("post/<int:pk>/del", PostDeleteView.as_view(), name="delete_post"),
]
