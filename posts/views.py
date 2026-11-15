from django.shortcuts import render, redirect, get_object_or_404
from .models import Post


# Lista de publicações
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts/post_list.html', {'posts': posts})


# Página individual de uma publicação
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/post_detail.html', {'post': post})


# Criar publicação
def post_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        Post.objects.create(title=title, content=content)
        return redirect('post_list')

    return render(request, 'posts/post_form.html', {'titulo': 'Criar publicação'})


# Editar publicação
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()

        return redirect('post_detail', pk=post.pk)

    return render(request, 'posts/post_form.html', {
        'post': post,
        'titulo': 'Editar publicação'
    })


# Excluir publicação
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('post_list')

    return render(request, 'posts/post_confirm_delete.html', {'post': post})
