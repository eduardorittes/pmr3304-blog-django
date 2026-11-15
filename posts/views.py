from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Comment
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm


# Lista de publicações
class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']


# Página individual de publicação
class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'


# Criar publicação
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html'
    success_url = reverse_lazy('post_list')
    extra_context = {'titulo': 'Criar publicação'}


# Editar publicação
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html'
    success_url = reverse_lazy('post_list')
    extra_context = {'titulo': 'Editar publicação'}


# Excluir publicação
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/post_confirm_delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('post_list')

# Criar comentario
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