from django.contrib import admin
from django.urls import path
from .views import ArticleView, HomepageView

urlpatterns = [
    path('', HomepageView.as_view(), name="homepage"),
    path('article/<int:pk>', ArticleView.as_view(), name="article"),
]
