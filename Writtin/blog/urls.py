from django.contrib import admin
from django.urls import path
from .views import ArticleView, AddArticleView, HomepageView, UpdateArticleView, DeleteArticleView

urlpatterns = [
    path('', HomepageView.as_view(), name="homepage"),
    path('article/<int:pk>', ArticleView.as_view(), name="article"),
    path('add_article/', AddArticleView.as_view(), name="add_article"),
    path('update_article/<int:pk>',
         UpdateArticleView.as_view(), name="update_article"),
    path('article/<int:pk>/delete',
         DeleteArticleView.as_view(), name="delete_article"),
]
