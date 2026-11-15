from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Post, Comment, Category
from .forms import PostForm


# LISTAGEM DE POSTS

class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']


# DETALHES DO POST

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'


# CRIAR POST

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html'
    success_url = reverse_lazy('post_list')
    extra_context = {'titulo': 'Criar publicação'}


# EDITAR POST

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html'
    success_url = reverse_lazy('post_list')
    extra_context = {'titulo': 'Editar publicação'}


# EXCLUIR POST

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/post_confirm_delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('post_list')


# CRIAR COMENTARIO

@login_required
def comment_create(request, pk):

    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':

        text = request.POST.get('text', '').strip()

        if text:
            Comment.objects.create(
                post=post,
                author=request.user,
                text=text
            )

            return redirect('post_detail', pk=post.pk)

        return render(request, 'posts/comment_form.html', {
            'post': post,
            'erro': 'Digite um comentario antes de enviar.'
        })

    return render(request, 'posts/comment_form.html', {
        'post': post
    })


# LISTAGEM DE CATEGORIAS

class CategoryListView(ListView):
    model = Category
    template_name = 'posts/category_list.html'
    context_object_name = 'categories'


# POSTS DE UMA CATEGORIA

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'posts/post_list.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['posts'] = self.object.posts.all().order_by(
            '-created_at'
        )

        return context