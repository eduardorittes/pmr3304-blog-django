from django.urls import path

from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    comment_create
)

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),

    path('post/<int:pk>/',
         PostDetailView.as_view(), name='post_detail'),

    path('novo/',
         PostCreateView.as_view(), name='post_create'),

    path('post/<int:pk>/editar/',
         PostUpdateView.as_view(), name='post_update'),

    path('post/<int:pk>/excluir/',
         PostDeleteView.as_view(), name='post_delete'),

    path('post/<int:pk>/comentar/',
         comment_create, name='comment_create'),
]