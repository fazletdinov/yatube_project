from django.shortcuts import render, get_object_or_404
# Импортируем модель, чтобы обратиться к ней
from .models import Post, Group


def index(request):
    posts = Post.objects.all()[:10]
    context = {
        'posts': posts,
        'title': 'Последние обновления на сайте'
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group)[:10]

    context = {
        'group': group,
        'posts': posts,
        'title': 'Записи сообщества '
    }
    return render(request, template, context)
