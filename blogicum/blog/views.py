from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import Http404
from .models import Post, Category


def index(request):
    """View функция - лента записей."""
    template = 'blog/index.html'

    posts = Post.objects.select_related(
        "author",
        "location",
        "category",
    ).filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now(),
    )

    context = {
        "posts": posts[:5],
    }

    return render(
        request=request,
        template_name=template,
        context=context,
    )


def post_detail(request, post_id):
    """View функция - конкретно выбранная запись в ленте."""
    template = 'blog/detail.html'

    current_post = get_object_or_404(
        Post.objects.select_related('category'),
        pk=post_id,
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True,
    )

    context = {
        "post": current_post,
    }

    return render(
        request=request,
        template_name=template,
        context=context,
    )


def category_posts(request, category_slug):
    """View функция - категория постов."""
    template = 'blog/category.html'

    try:

        current_category = Category.objects.get(slug=category_slug)

        if not current_category.is_published:
            raise Http404("Неизвестная категория")

        posts = Post.objects.filter(
            category=current_category,
            is_published=True,
            pub_date__lte=timezone.now(),
        ).order_by(
            '-pub_date',
        )

    except Category.DoesNotExist:
        raise Http404("Категория не найдена.")

    context = {
        "category": current_category,
        "posts": posts,
    }

    return render(
        request=request,
        template_name=template,
        context=context,
    )
