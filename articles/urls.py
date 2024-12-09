from django.urls import path

from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleUpdateView,
    ArticleDeleteView,
    ArticleCreateView,
    ArticleListAPIView,
    ArticleDetailAPIView,
    CommentListCreateAPIView,
    CommentDetailAPIView,
)

urlpatterns = [
    path("<int:pk>/", ArticleDetailView.as_view(), name="article_detail"),
    path("<int:pk>/edit/", ArticleUpdateView.as_view(), name="article_edit"),
    path("<int:pk>/delete/", ArticleDeleteView.as_view(), name="article_delete"),
    path("new/", ArticleCreateView.as_view(), name="article_new"),
    path("", ArticleListView.as_view(), name="article_list"),
    # REST
    path('api/posts/', ArticleListAPIView.as_view(), name='article_list_create_api'),
    path('api/posts/<int:pk>/', ArticleDetailAPIView.as_view(), name='article_detail_api'),
    path('api/posts/<int:pk>/comments/', CommentListCreateAPIView.as_view(), name='comment_list_create_api'),
    path('api/comments/<int:pk>/', CommentDetailAPIView.as_view(), name='comment_detail_api'),

]
